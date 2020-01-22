import random

# Initialize game board
A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# define available user options (u,d,l,r)

choicelist = [0,1,2,3]

#choose to spawn a 4 or 2 according to game rules probability
Pspawn=random.uniform(0,1)
#print("Pspawn");print(Pspawn)
if Pspawn >= .8:
    A[random.choice(choicelist)][random.choice(choicelist)]=4
else:
    A[random.choice(choicelist)][random.choice(choicelist)]=2

#grab user choice and begin logic
def move(A,input):

    # broken
    if input == "u":
        n=0

        # loop over columns
        for m in range(0,4):

            # if any on a column are not zero:
            if A[n][m]!=0 or A[n+1][m]!=0 or A[n+2][m]!=0 or A[n+3][m]!=0:

                # if the nu
                if A[n][m]==0:
                    while A[n][m]==0:
                        A[n][m]=A[n+1][m]
                        A[n+1][m]=A[n+2][m]
                        A[n+2][m] = A[n+3][m]
                        A[n+3][m]=0
                if A[n+1][m]==0 and (A[n+2][m]!=0 or A[n+3][m]!=0):
                    while A[n+1][m]==0:
                        A[n+1][m]=A[n+2][m]
                        A[n+2][m]=A[n+3][m]
                        A[n+3][m]=0
                if A[n+2][m]==0 and (A[n+3][m]!=0):
                    while A[n+2][m]==0:
                        A[n+2][m]=A[n+3][m]
                        A[n+3][m]=0
        n=0
        for m in range(0,4):
            if A[n][m]==A[n+1][m]:
                A[n][m]=A[n][m]+A[n+1][m]
                A[n+1][m]=A[n+2][m]
                A[n+2][m]=A[n+3][m]
                A[n+3][m]=0
            if A[n+1][m]==A[n+2][m]:
                A[n+1][m]=A[n+1][m]+A[n+2][m]
                A[n+2][m]=A[n+3][m]
                A[n+3][m]=0
            if A[n+2][m]==A[n+3][m]:
                A[n+2][m]=A[n+2][m]+A[n+3][m]
                A[n+3][m]=0
    #broken
    elif input == "d":

        # reinitialize firsfirst t to row
        n=0

        #loop over columns
        for m in range(0,4):
            if A[n][m]!=0 or A[n+1][m]!=0 or A[n+2][m]!=0 or A[n+3][m]!=0:
                if A[n+3][m]==0:
                    while A[n+3][m]==0:
                        A[n+3][m]=A[n+2][m]
                        A[n+2][m]=A[n+1][m]
                        A[n+1][m]=A[n][m]
                        A[n][m]=0
                if A[n+2][m]==0 and (A[n+1][m]!=0 or A[n][m]!=0):
                    while A[n+2][m]==0:
                        A[n+2][m]=A[n+1][m]
                        A[n+1][m]=A[n][m]
                        A[n][m]=0
                if A[n+1][m]==0 and A[n][m]!=0:
                    while A[n+1][m]==0:
                        A[n+1][m]=A[n][m]
                        A[n][m]=0

        # reinitialize to first
        n=0
        for m in range(0,4):
            if A[n+3][m]==A[n+2][m]:
                A[n+3][m]=A[n+3][m] + A[n+2][m]
                A[n+2][m]=A[n+1][m]
                A[n+1][m]=A[n][m]
                A[n][m]=0
            if A[n+2][m]==A[n+1][m]:
                A[n+2][m]=A[n+2][m]+A[n+1][m]
                A[n+1][m]=A[n][m]
                A[n][m]=0
            if A[n+1][m]==A[n][m]:
                A[n+1][m]=A[n+1][m]+A[n][m]
                A[n][m]=0
    elif input == "l":
        m=0
        for n in range(0,4):
            if A[n][m]!=0 or A[n][m+1]!=0 or A[n][m+2]!=0 or A[n][m+3]!=0:
                if A[n][m]==0:
                    while A[n][m]==0:
                        A[n][m]=A[n][m+1]
                        A[n][m+1]=A[n][m+2]
                        A[n][m+2] = A[n][m+3]
                        A[n][m+3]=0
            if A[n][m+1]==0 and (A[n][m+2]!=0 or A[n][m+3]!=0):
                while A[n][m+1]==0:
                    A[n][m+1]=A[n][m+2]
                    A[n][m+2]=A[n][m+3]
                    A[n][m+3]=0
            if A[n][m+2]==0 and (A[n][m+3]!=0):
                while A[n][m+2]==0:
                    A[n][m+2]=A[n][m+3]
                    A[n][m+3]=0
        m=0
        for n in range(0,4):
            if A[n][m]==A[n][m+1]:
                A[n][m]=A[n][m]+A[n][m+1]
                A[n][m+1]=A[n][m+2]
                A[n][m+2]=A[n][m+3]
                A[n][m+3]=0
            if A[n][m+1]==A[n][m+2]:
                A[n][m+1]=A[n][m+1]+A[n][m+2]
                A[n][m+2]=A[n][m+3]
                A[n][m+3]=0
            if A[n][m+2]==A[n][m+3]:
                A[n][m+2]=A[n][m+2]+A[n][m+3]
                A[n][m+3]=0
    elif input == "r":
        m=0

        #loop over rows
        for n in range(0,4):
            if A[n][m]!=0 or A[n][m+1]!=0 or A[n][m+2]!=0 or A[n][m+3]!=0:
                if A[n][m+3]==0:
                    while A[n][m+3]==0:
                        A[n][m+3]=A[n][m+2]
                        A[n][m+2]=A[n][m+1]
                        A[n][m+1]=A[n][m]
                        A[n][m]=0
            if A[n][m+2]==0 and (A[n][m+1]!=0 or A[n][m]!=0):
                while A[n][m+2]==0:
                    A[n][m+2]=A[n][m+1]
                    A[n][m+1]=A[n][m]
                    A[n][m]=0
            if A[n][m+1]==0 and A[n][m]!=0:
                while A[n][m+1]==0:
                    A[n][m+1]=A[n][m]
                    A[n][m]=0
        m=0
        for n in range(0,4):
            if A[n][m+3]==A[n][m+2]:
                A[n][m+3]=A[n][m+3] + A[n][m+2]
                A[n][m+2]=A[n][m+1]
                A[n][m+1]=A[n][m]
                A[n][m]=0
            if A[n][m+2]==A[n][m+1]:
                A[n][m+2]=A[n][m+2]+A[n][m+1]
                A[n][m+1]=A[n][m]
                A[n][m]=0
            if A[n][m+1]==A[n][m]:
                A[n][m+1]=A[n][m+1]+A[n][m]
                A[n][m]=0

def ai_move(A):
    # Weight Matrix
    #W= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    input = random.choice(["u","d","l","r"])
    #print("autogenerated input");print(input)
    return input

def print_board(A):
    print(A[0][0],"\t",A[0][1],"\t",A[0][2],"\t",A[0][3],"\n")
    print(A[1][0],"\t",A[1][1],"\t",A[1][2],"\t",A[1][3],"\n")
    print(A[2][0],"\t",A[2][1],"\t",A[2][2],"\t",A[2][3],"\n")
    print(A[3][0],"\t",A[3][1],"\t",A[3][2],"\t",A[3][3],"\n")
    return

#main program loop
while True:
    #call ai_move function to generate input for game logic
    input=ai_move(A)

    #IF the user is playing the game manually:
    #print("input");print(input)
    #while input == ""
    #    input = raw_input("u for upward direction, d for downwards, l for left and r for Right")

    #send input to game logic
    move(A,input)


    #check for open tiles
    listforn = []
    listform = []
    zeros = 0
    for n in range(0,4):
        for m in range(0,4):
            if A[n][m]==0:
                zeros+=1
                listforn.append(n)
                listform.append(m)

    #print number of open tiles
    #print("zeros");print(zeros)

    #if there are open tiles
    if zeros > 0:

        #if there are multiple open tiles
        if zeros >= 1:

            #spawn a 2 or 4 in a random spot according to game rules probability
            randomindex = listforn.index(random.choice(listforn))
            Pspawn=random.uniform(0,1)
            #print("Pspawn");print(Pspawn)
            if Pspawn >= .8:
                A[listforn[randomindex]][listform[randomindex]]=4
            else:

                A[listforn[randomindex]][listform[randomindex]]=2


    else: # there are no open tiles
        print("Game over")

        #print the final game state
        print_board(A)

        break

# minimax

# attempt to exploit the monte-carlo algorithm
#     -general-purpose solver
#     -heuristic search algorithm
#     -apply the most promising moves
#Determine most promising move:











