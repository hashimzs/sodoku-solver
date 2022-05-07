board=[
[7,8,0,4,0,1,0,2,7],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7]
       ]
def display_board(bo):

    for i in range(len(bo)):
        if (i % 3)==0 and i!=0:
            print("----------------------------------")
        for j in range(len(bo[i])):
            if (j % 3)==0 and j != 0:
               print(" / ",end="")

            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+"  ",end="")

def find_empty(bo):
    empty_list=[]
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j]==0:
                empty_list.append([i,j])
    return empty_list

def valid(bo,num,pos):
    #check row
    for column in range(len(bo[0])):
        currrow = bo[pos[0]][column]
        if num == currrow and column != pos[1]:
            return False
    #check column
    for row in range(len(bo)):
        currcolumn = bo[row][pos[1]]
        if num == currcolumn and row != pos[0]:
                return False

    box_x=pos[0]//3
    box_y=pos[1]//3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if num==bo[i][j] and pos!=[i,j]:
                return False
    return True

def solver(bo):
    display_board2(bo)
    position=0
    correct = True
    count = 0
    empty = find_empty(board)
    curr = 0
    currrow = 0
    currcolumn = 0
    stage=0
    print("solution")
    while stage<(len(empty)):
        position = [empty[stage][0] , empty[stage][1]]
        curr=bo[position[0]][position[1]]
        while curr <= 9:
             correct = True
             curr +=1
             correct=valid(bo,curr,position)
             if correct == True:
                 bo[position[0]][position[1]]=curr
                 stage += 1
                 break
        if correct==False:
            stage+=-1
            bo[position[0]][position[1]]=0
    return bo


bo=solver(board)
display_board2(bo)

def display_board2(bo):

    for i in range(len(bo)):
        output = ""
        if (i % 3) == 0 and i != 0:
            print("----------------------------------")
        for j in range(len(bo[i])):
            if (j%3)==0 and j!=0:
               output+=" / "
            output+=str(bo[i][j])+" "
        print(output)






















