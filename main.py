def print_check(size):
    for i in range(0,size):
        for j in range(0,size):
            print(array2D[i][j],end=" ")
            if (j == (size -1)):
                print(" ")
               
def set_X(x,y):
    if(array2D[x-1][y-1] != ('X' and'Y')):
        array2D[x-1][y-1] = "X" 
def set_O(x,y):
    if(array2D[x-1][y-1] != ('X' and'Y')):
        array2D[x-1][y-1] = "O"
def judgement(size):
    for i in range(0,size):
        for j in range(0,size-4):
            if(array2D[i][j]==array2D[i][j+1]==array2D[i][j+2]==array2D[i][j+3]==array2D[i][j+4]==('X'or'O')):                
                return 1
    for i in range(0,size-4):
        for j in range(0,size):
            if(array2D[i][j]==array2D[i+1][j]==array2D[i+2][j]==array2D[i+3][j]==array2D[i+4][j]==('X'or'O')):
                return  1
    for i in range(0,size-4):
        for j in range(0,size-4):        
            if(array2D[i][j]==array2D[i+1][j+1]==array2D[i+2][j+2]==array2D[i+3][j+3]==array2D[i+4][j+4]==('X'or'O')):
                return  1
    for i in range(0,size-4):
        for j in range(0,size-4):                
            if(array2D[i][j+4]==array2D[i+2][j+2]==array2D[i+3][j+1]==array2D[i+4][j]==array2D[i+1][j+3]==('X'or'O')):
                return  1
def robot(size,x):
    for i in range(0,size):
        for j in range(0,size-3):
            if(array2D[i][j]==array2D[i][j+1]==array2D[i][j+2]==array2D[i][j+3]=='X'):                
                if(j == 0 and array2D[i][j+4] == '.' ):
                    array2D[i][j+4] = 'O'
                elif(j == 11 and array2D[i][j-1] == '.' ):
                    array2D[i][j-1] = 'O' 
                elif(j > 0 and j <11):
                    if(array2D[i][j-1] == 'O' and array2D[i][j+4] == '.' ):
                        array2D[i][j+4] = 'O' 
                    elif(array2D[i][j+4] == 'O' and array2D[i][j-1] == '.' ):
                        array2D[i][j-1] = 'O'
                    elif(array2D[i][j+4] == '.' and array2D[i][j-1] == '.' ):
                        array2D[i][j-1] = 'O'    
            elif(j<11):
                if(array2D[i][j]==array2D[i][j+1]==array2D[i][j+2]==array2D[i][j+4]=='X'):                
                    array2D[i][j+3] = 'O' 
                elif(array2D[i][j]==array2D[i][j+1]==array2D[i][j+3]==array2D[i][j+4]=='X'):                
                    array2D[i][j+2] = 'O'
                elif(array2D[i][j]==array2D[i][j+3]==array2D[i][j+2]==array2D[i][j+4]=='X'):                
                    array2D[i][j+3] = 'O' 
            else:
                x = 0
    if(x == 0):
        for i in range(0,size-3):
            for j in range(0,size):
                if(array2D[i][j]==array2D[i+1][j]==array2D[i+2][j]==array2D[i+3][j]=='X'):                
                    if(i == 0 and array2D[i+4][j] == '.' ):
                        array2D[i+4][j] = 'O'
                    elif(i == 11 and array2D[i-1][j] == '.' ):
                        array2D[i-1][j] = 'O' 
                    elif(i > 0 and i <11):
                        if(array2D[i-1][j] == 'O' and array2D[i+4][j] == '.' ):
                            array2D[i+4][j] = 'O' 
                        elif(array2D[i+4][j] == 'O' and array2D[i-1][j] == '.' ):
                            array2D[i-1][j] = 'O'
                        elif(array2D[i+4][j] == '.' and array2D[i-1][j] == '.' ):
                            array2D[i-1][j] = 'O'    
                elif(i<11):
                    if(array2D[i][j]==array2D[i+1][j]==array2D[i+2][j]==array2D[i+4][j]=='X'):                
                        array2D[i+3][j] = 'O' 
                    elif(array2D[i][j]==array2D[i+1][j]==array2D[i+4][j]==array2D[i+3][j]=='X'):                
                        array2D[i+2][j] = 'O'
                    elif(array2D[i][j]==array2D[i+4][j]==array2D[i+2][j]==array2D[i+3][j]=='X'):              
                        array2D[i+2][j] = 'O' 
                
                else

                   

    
    












shutdown = 0
size = 15
array2D = [["." for _ in range(size)] for _ in range(size)]        
while shutdown ==0:
    x = 1
    print_check(size) 
    print("X turn")
    x = int(input("x-axis")) 
    y = int(input("y-axis"))
    set_X(y,x)
    
    if(judgement(size) == 1):
        shutdown = judgement(size)
        print_check(size)
        print('X win')
        
    else:
        print_check(size) 
        robot(size,x)
        if(judgement(size) == 1):
            shutdown = judgement(size)
            print_check(size)
            print('O win')

