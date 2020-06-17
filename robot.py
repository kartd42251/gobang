import random 
from game_basic import *

def random_init(array2D):
    for i in range(30):
        x = random.randint(1,15)
        y = random.randint(1,15)
        set_X(array2D,x,y)
def manual_init(array2D):
    for i in range(7,11):
        set_X(array2D,i,5)
def eva2(array2D,x,y):
    if( x > 14 or x < 0 or y > 14 or y < 0):
        return 0
    if(array2D[x][y] != 'X') :
        return 0
    return 1+eva2(array2D,x+1,y)
    #+eva2(array2D,x-1,y)+eva2(array2D,x,y+1)+eva2(array2D,x,y-1)\
    #        +eva2(array2D,x+1,y+1)+eva2(array2D,x+1,y-1)+eva2(array2D,x-1,y+1)+eva2(array2D,x-1,y-1)  
def eva(array2D,x,y):
    if(array2D[x][y] == 'O'):
        return 0
    #4
    if( x-4 >= 0 and array2D[x-1][y] == array2D[x-2][y] == array2D[x-3][y] == array2D[x-4][y] == 'X' ):
        return 14
    if( x+4 <= 14 and array2D[x+1][y] == array2D[x+2][y] == array2D[x+3][y] == array2D[x+4][y] == 'X'):
        return 14
    if( y-4 >= 0 and array2D[x][y-1] == array2D[x][y-2] == array2D[x][y-3] == array2D[x][y-4] == 'X' ):
        return 14
    if( y+4 <= 14 and array2D[x][y+1] == array2D[x][y+2] == array2D[x][y+3] == array2D[x][y+4] == 'X'):
        return 14
    #4
    if( x-4 >= 0 and y-4 >= 0 and array2D[x-1][y-1] == array2D[x-2][y-2] == array2D[x-3][y-3] == array2D[x-4][y-4] == 'X' ):
        return 14
    if( x+4 <= 14 and y+4 <= 14 and array2D[x+1][y+1] == array2D[x+2][y+2] == array2D[x+3][y+3] == array2D[x+4][y+4] == 'X'):
        return 14
    if( y-4 >= 0 and x+4 <= 14 and array2D[x+1][y-1] == array2D[x+2][y-2] == array2D[x+3][y-3] == array2D[x+4][y-4] == 'X' ):
        return 14
    if( y+4 <= 14 and x-4 >= 0 and array2D[x-1][y+1] == array2D[x-2][y+2] == array2D[x-3][y+3] == array2D[x-4][y+4] == 'X'):
        return 14
    
    #3 in a row
    if( x-3 >= 0 and array2D[x-1][y] == array2D[x-2][y] == array2D[x-3][y] == 'X' ):
        if(x-4 >= 0 and array2D[x-4][y] == 'O'):
            return 0
        return 10
    if( x+3 <= 14 and array2D[x+1][y] == array2D[x+2][y] == array2D[x+3][y] == 'X'):
        if(x+4 <= 14 and array2D[x+4][y] == 'O'):
            return 0
        return 10
    if( y-3 >= 0 and array2D[x][y-1] == array2D[x][y-2] == array2D[x][y-3] == 'X' ):
        if(y-4 >= 0 and array2D[x][y-4] == 'O'):
            return 0
        return 10
    if( y+3 <= 14 and array2D[x][y+1] == array2D[x][y+2] == array2D[x][y+3] == 'X'):
        if(y+4 <= 14 and array2D[x][y+4] == 'O'):
            return 0
        return 10
    #3
    if( x-3 >= 0 and y-3 >= 0 and array2D[x-1][y-1] == array2D[x-2][y-2] == array2D[x-3][y-3] == 'X' ):
        if(x-4 >= 0 and y-4 >= 0 and array2D[x-4][y-4] == 'O'):
            return 0
        return 10
    if( x+3 <= 14 and y+3 <= 14 and array2D[x+1][y+1] == array2D[x+2][y+2] == array2D[x+3][y+3] == 'X'):
        if(x+4 <= 14 and y+4 <= 14 and array2D[x+4][y+4] == 'O'):
            return 0
        return 10
    if( y-3 >= 0 and x+3 <= 14 and array2D[x+1][y-1] == array2D[x+2][y-2] == array2D[x+3][y-3] == 'X' ):
        if(y-4 >= 0 and x+4 <= 14 and array2D[x+4][y-4] == 'O'):
            return 0
        return 10
    if( y+3 <= 14 and x-3 >= 0 and array2D[x-1][y+1] == array2D[x-2][y+2] == array2D[x-3][y+3] == 'X'):
        if(x-4 >= 0 and y+4 <= 14 and array2D[x-4][y+4] == 'O'):
            return 0
        return 10
    #2 in a row
    if( x-2 >= 0 and array2D[x-1][y] == array2D[x-2][y] == 'X' ):
        if(x-3 >= 0 and array2D[x-3][y] == 'O'):
            return 0
        return 7
    if( x+2 <= 14 and array2D[x+1][y] == array2D[x+2][y] == 'X'):
        if(x+3 <= 14 and array2D[x+3][y] == 'O'):
            return 0
        return 7
    if( y-2 >= 0 and array2D[x][y-1] == array2D[x][y-2] == 'X' ):
        if(y-3 >= 0 and array2D[x][y-3] == 'O'):
            return 0
        return 7
    if( y+2 <= 14 and array2D[x][y+1] == array2D[x][y+2] == 'X'):
        if(y+3 >= 0 and array2D[x][y+3] == 'O'):
            return 0
        return 7 
    #2
    if( x-2 >= 0 and y-2 >= 0 and array2D[x-1][y-1] == array2D[x-2][y-2] == 'X' ):
        if(x-3 >= 0 and y-3 >= 0 and array2D[x-3][y-3] == 'O'):
            return 0
        return 7
    if( x+2 <= 14 and y+2 <= 14 and array2D[x+1][y+1] == array2D[x+2][y+2] == 'X'):
        if(x+3 <= 14 and y+3 <= 14 and array2D[x+3][y+3] == 'O'):
            return 0
        return 7
    if( y-2 >= 0 and x+2 <= 14 and array2D[x+1][y-1] == array2D[x+2][y-2] == 'X' ):
        if(y-3 >= 0 and x+3 <= 14 and array2D[x+3][y-3] == 'O'):
            return 0
        return 7
    if( y+2 <= 14 and x-2 >= 0 and array2D[x-1][y+1] == array2D[x-2][y+2] == 'X'):
        if(y+3 <= 14 and x-3 >= 0 and array2D[x-3][y+3] == 'O'):
            return 0
        return 7    
    #only 1
    if( x+1 <= 14 and array2D[x+1][y] == 'X' ):
        if(x+2 <= 14 and array2D[x+2][y] == 'O'):
            return 0
        return 2
    if( x-1 >=0 and array2D[x-1][y] == 'X'):
        if(x-2 >= 0 and array2D[x-2][y] == 'O'):
            return 0
        return 2
    if( y-1 >= 0 and array2D[x][y-1] == 'X' ):
        if(y-2 >= 0 and array2D[x][y-2] == 'O'):
            return 0
        return 2
    if( y+1 <= 14 and array2D[x][y+1] == 'X'):
        if(y+2 <= 14 and array2D[x][y+2] == 'O'):
            return 0
        return 2
    #1
    if( x+1 <= 14 and y+1 <= 14 and array2D[x+1][y+1] == 'X' ):
        if(x+2 <= 14 and y+2 <= 14 and array2D[x+2][y+2] == 'O'):
            return 0
        return 2
    if( x-1 >=0 and y-1 >= 0 and array2D[x-1][y-1] == 'X'):
        if(x-2 >= 0 and y-2 >= 0 and array2D[x-2][y-2] == 'O'):
            return 0
        return 2
    if( y-1 >= 0 and x+1 <= 14 and array2D[x+1][y-1] == 'X' ):
        if(y-2 >= 0 and x+2 <= 14 and array2D[x+2][y-2] == 'O'):
            return 0
        return 2
    if( y+1 <= 14 and x-1 >= 0 and array2D[x-1][y+1] == 'X'):
        if(y+2 <= 14 and x-2 >= 0 and array2D[x-2][y+2] == 'O'):
            return 0
        return 2
    return 0


def eva3(array2D,size): 
    eva_result = [[0 for _ in range(size)] for _ in range(size)]
    _max = -1
    i_max = -1
    j_max = -1
    for i in range(0,size):
        for j in range(0,size):
            Sum = 0
            if(array2D[i][j] == '.'):
                if(eva5(Sum,array2D,i,j)>=eva4(Sum,array2D,i,j)):
                    eva_result[i][j] = eva5(Sum,array2D,i,j)
                else:eva_result[i][j] = eva4(Sum,array2D,i,j)    
    for i in range(0,size):
        for j in range(0,size):
            print(eva_result[i][j],end = ' ')
        print()
    for i in range(0,size):
        for j in range(0,size):
            if(eva_result[i][j] > _max):
                _max = eva_result[i][j]
                i_max = i
                j_max = j
    print(i_max,j_max)
    
    return i_max+1,j_max+1

def eva4(Sum,array2D,x,y):
    Sum = 0
    if(x<12 and x>2 and y<12 and y>2 ):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):    
            if(array2D[x][y-k]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'):
                Sum += k*(k-1)*(2*k-1)/6
                break
        return Sum            


    else:
        return  0  


def eva5(Sum,array2D,x,y):
    Sum = 0
    if(x<12 and x>2 and y<12 and y>2 ):
        for k in range(1,6):
            if(array2D[x][y+k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):    
            if(array2D[x][y-k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='O'):
                Sum += k*(k-1)/2
                break
        return Sum            


    else:
        return  0  








    