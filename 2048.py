import random
import math
import operator
import numpy as np
import copy

#random.seed(12345)
sage_server.MAX_OUTPUT=1e6

def spawn(N):
    #check for open tiles
    listforn = []
    listform = []
    zeros = 0
    for n in range(0,4):
        for m in range(0,4):
            if N[n][m]==0:
                zeros=zeros+1
                listforn.append(n)
                listform.append(m)
    if zeros > 0:
        if zeros >=1:
            randomindex = listforn.index(random.choice(listforn))
            Pspawn = random.choice(srange(5))/5
            if Pspawn >= .8:
                N[listforn[randomindex]][listform[randomindex]]=4
            else:
                N[listforn[randomindex]][listform[randomindex]]=2
    return N;

def print_board(N):
    print N[0][0],"\t",N[0][1],"\t",N[0][2],"\t",N[0][3],"\n"
    print N[1][0],"\t",N[1][1],"\t",N[1][2],"\t",N[1][3],"\n"
    print N[2][0],"\t",N[2][1],"\t",N[2][2],"\t",N[2][3],"\n"
    print N[3][0],"\t",N[3][1],"\t",N[3][2],"\t",N[3][3],"\n"
    return

def move(B,input):
    if input == "u":
        n=0
        # loop over columns
        for m in range(0,4):
            # if any on a column are not zero:
            if B[n][m]!=0 or B[n+1][m]!=0 or B[n+2][m]!=0 or B[n+3][m]!=0:
                # if the first element in the column is zero
                if B[n][m]==0:
                    # while the top tile is zero
                    while B[n][m]==0:
                        #assign tile below's value to top tile in column
                        #Get rid of these hardcoded indices
                        B[n][m]=B[n+1][m]
                        B[n+1][m]=B[n+2][m]
                        B[n+2][m] = B[n+3][m]
                        B[n+3][m]=0
                if B[n+1][m]==0 and (B[n+2][m]!=0 or B[n+3][m]!=0):
                    while B[n+1][m]==0:
                        B[n+1][m]=B[n+2][m]
                        B[n+2][m]=B[n+3][m]
                        B[n+3][m]=0
                if B[n+2][m]==0 and (B[n+3][m]!=0):
                    while B[n+2][m]==0:
                        B[n+2][m]=B[n+3][m]
                        B[n+3][m]=0
        n=0
        for m in range(0,4):
            if B[n][m]==B[n+1][m]:
                B[n][m]=B[n][m]+B[n+1][m]
                B[n+1][m]=B[n+2][m]
                B[n+2][m]=B[n+3][m]
                B[n+3][m]=0
            if B[n+1][m]==B[n+2][m]:
                B[n+1][m]=B[n+1][m]+B[n+2][m]
                B[n+2][m]=B[n+3][m]
                B[n+3][m]=0
            if B[n+2][m]==B[n+3][m]:
                B[n+2][m]=B[n+2][m]+B[n+3][m]
                B[n+3][m]=0

    #user inputs down
    elif input == "d":
        # in this loop we collapse the matrix in the specified direction
        n=0
        #loop over columns
        for m in range(0,4):
            # if any tiles in that column are not zero
            if B[n][m]!=0 or B[n+1][m]!=0 or B[n+2][m]!=0 or B[n+3][m]!=0:
                # if bottom tile in column is zero
                if B[n+3][m]==0:
                    # collapse column completely
                    while B[n+3][m]==0:
                        B[n+3][m]=B[n+2][m]
                        B[n+2][m]=B[n+1][m]
                        B[n+1][m]=B[n][m]
                        B[n][m]=0
                # if second from bottom tile is zero and nonzero above
                if B[n+2][m]==0 and (B[n+1][m]!=0 or B[n][m]!=0):
                    # collapse column to second from bottom tile
                    while B[n+2][m]==0:
                        B[n+2][m]=B[n+1][m]
                        B[n+1][m]=B[n][m]
                        B[n][m]=0
                # if top tile in column can slide down one space
                if B[n+1][m]==0 and B[n][m]!=0:
                    # move top tile down one
                    while B[n+1][m]==0:
                        B[n+1][m]=B[n][m]
                        B[n][m]=0
        n=0
        # This loop merges identical tiles in the specified direction
        # loop over columns again
        for m in range(0,4):
            if B[n+3][m]==B[n+2][m]:
                B[n+3][m]=B[n+3][m] + B[n+2][m]
                B[n+2][m]=B[n+1][m]
                B[n+1][m]=B[n][m]
                B[n][m]=0
            if B[n+2][m]==B[n+1][m]:
                B[n+2][m]=B[n+2][m]+B[n+1][m]
                B[n+1][m]=B[n][m]
                B[n][m]=0
            if B[n+1][m]==B[n][m]:
                B[n+1][m]=B[n+1][m]+B[n][m]
                B[n][m]=0

    elif input == "l":
        m=0
        for n in range(0,4):
            if B[n][m]!=0 or B[n][m+1]!=0 or B[n][m+2]!=0 or B[n][m+3]!=0:
                if B[n][m]==0:
                    while B[n][m]==0:
                        B[n][m]=B[n][m+1]
                        B[n][m+1]=B[n][m+2]
                        B[n][m+2] = B[n][m+3]
                        B[n][m+3]=0
            if B[n][m+1]==0 and (B[n][m+2]!=0 or B[n][m+3]!=0):
                while B[n][m+1]==0:
                    B[n][m+1]=B[n][m+2]
                    B[n][m+2]=B[n][m+3]
                    B[n][m+3]=0
            if B[n][m+2]==0 and (B[n][m+3]!=0):
                while B[n][m+2]==0:
                    B[n][m+2]=B[n][m+3]
                    B[n][m+3]=0

        m=0
        for n in range(0,4):
            if B[n][m]==B[n][m+1]:
                B[n][m]=B[n][m]+B[n][m+1]
                B[n][m+1]=B[n][m+2]
                B[n][m+2]=B[n][m+3]
                B[n][m+3]=0
            if B[n][m+1]==B[n][m+2]:
                B[n][m+1]=B[n][m+1]+B[n][m+2]
                B[n][m+2]=B[n][m+3]
                B[n][m+3]=0
            if B[n][m+2]==B[n][m+3]:
                B[n][m+2]=B[n][m+2]+B[n][m+3]
                B[n][m+3]=0

    elif input == "r":
        m=0
        #loop over rows
        for n in range(0,4):
            if B[n][m]!=0 or B[n][m+1]!=0 or B[n][m+2]!=0 or B[n][m+3]!=0:
                if B[n][m+3]==0:
                    while B[n][m+3]==0:
                        B[n][m+3]=B[n][m+2]
                        B[n][m+2]=B[n][m+1]
                        B[n][m+1]=B[n][m]
                        B[n][m]=0
            if B[n][m+2]==0 and (B[n][m+1]!=0 or B[n][m]!=0):
                while B[n][m+2]==0:
                    B[n][m+2]=B[n][m+1]
                    B[n][m+1]=B[n][m]
                    B[n][m]=0
            if B[n][m+1]==0 and B[n][m]!=0:
                while B[n][m+1]==0:
                    B[n][m+1]=B[n][m]
                    B[n][m]=0
        m=0
        for n in range(0,4):
            if B[n][m+3]==B[n][m+2]:
                B[n][m+3]=B[n][m+3] + B[n][m+2]
                B[n][m+2]=B[n][m+1]
                B[n][m+1]=B[n][m]
                B[n][m]=0
            if B[n][m+2]==B[n][m+1]:
                B[n][m+2]=B[n][m+2]+B[n][m+1]
                B[n][m+1]=B[n][m]
                B[n][m]=0
            if B[n][m+1]==B[n][m]:
                B[n][m+1]=B[n][m+1]+B[n][m]
                B[n][m]=0
    return B

def check_possible(N, input, b):
    # Move is possible if, for any row, there are zeros in front of a number, or there are two adjacent matching numbers
        # return true if, for any check_vec
                    # tile after zero
                    # adjacent identical tiles

    #extract vectors to check
    check_vecs=[[] for _ in srange(b)];
    if input == "u":
        # for each check vec needed
        for j in range(0,b):
            #extract the check vec
            for i in srange(0,b):
                check_vecs[j].append(N[i][j])

    elif input == "d":
        #same as up
        for j in range(0,b):
            for i in srange(0,b):
                check_vecs[j].append(N[i][j])
        #but reverse them
        i=0
        for i in range(0,b):
            list.reverse(check_vecs[i])

    elif input == "l":
        for j in range(0,b):
            for i in range(0,b):
                check_vecs[j].append(N[j][i])

    elif input=="r":
        for j in range(0,b):
            for i in range(0,b):
                check_vecs[j].append(N[j][i])
        i=0
        for i in range(0,b):
            list.reverse(check_vecs[i])
    #print("check_vecs = ");print(check_vecs);

    #check the vectors
    for vec in check_vecs:
        #print("checking vector:");print(vec)

        #if no tile()s) in vec, all zeros, no move possible, move on to next check vec
        if np.any(vec)==False:
            continue

        # find the first zero
        zero_spot=[]
        try:
            zero_spot = vec.index(0)
        except ValueError:
            #print('no zeros in vec')
            zero_spot=[]

            i=0
            for i in range(0,b-1):
                if vec[i]!=0 and vec[i+1]!=0:
                    if vec[i]==vec[i+1]:
                        #we have a pair, move is possible
                        #print("mergable pair found")
                        return True

        #if there is a zero, check for tile after zero
        if zero_spot !=[]:
            i=0
            for i in range(zero_spot+1,b):
                #if hit a number, move is possible
                if vec[i]!=0:
                    return True

        #always check for mergers
        i=0
        for i in range(0,b-1):
            if vec[i]!=0 and vec[i+1]!=0:
                if vec[i]==vec[i+1]:
                    #we have a pair, move is possible
                    #print("mergable pair found")
                    return True
    # if you made it out of the check_vecs[vec] for loop, selectedmove is not possible
    return False

def game_over(N,b):
    #print("## checking if game is over ###");
    if check_possible(N,"u",b)==False and check_possible(N,"d",b)==False and check_possible(N,"l",b)==False and check_possible(N,"r",b)==False:
        #print("game over! result:")
        #print_board(N)
        return True
    else:
        return False

def score_board(N):
    score=0.0
    for n in range(0,4):
        for m in range(0,4):
            if N[n][m]!=0:
                c = N[n][m]
                score=score + c
    return score

def main(runs):
    print("score format: [up down left right]");print("")

    # Initialize game board #size bxb
    b=4
    A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];

    #spawn first tile
    A=spawn(A)

    while game_over(A,b)==False:

        starting_move = []
        scores=[]

        #print("######## MAIN BOARD ##########");
        print_board(A)
        #print("##############################");
        print("")

        for starting_move in ["u","d","l","r"]:
            # make a ***copy*** of board. A_=A is only references A and calling A_=move(A_) changes actual board A as well even though move() is written using only local variables!!!!!!
            A_=copy.deepcopy(A)

            if check_possible(A_,starting_move,b)==True:
                #print("starting_move");print(starting_move)
                A_=move(A_,starting_move)
                A_=spawn(A_)

                random_scores=[]
                m=0
                #play runs number of games using random moves and average the final scores
                for m in srange(0,runs):
                    A__=copy.deepcopy(A_)
                    while game_over(A__,b)==False:
                        random_move=random.choice(["u","d","l","r"])
                        if check_possible(A__,random_move,b)==True:
                            A__=move(A__,random_move)
                            A__=spawn(A__)
                    random_scores.append(score_board(A__))

                scores.append(sum(random_scores)/runs)
            else:
                #print('starting move not possible')
                scores.append(0)
                continue

        # print scores for simulated games
        print("scores:");print(scores);print("")

        # find move which netted the highest score
        index, value = max(enumerate(scores), key=operator.itemgetter(1))
        #print("index");print(index);print("")

        # write result of tree search to actual game board
        if index ==0:
            auto_input="u"
        elif index ==1:
            auto_input="d"
        elif index ==2:
            auto_input ="l"
        elif index ==3:
            auto_input ="r"
        #print("auto generated input:");print(auto_input);print("")

        # make real move
        A=move(A,auto_input)
        A=spawn(A)

    print("")
    print("Main BOARD: Final Game State")
    print("")
    print_board(A)

main(runs = 5)
