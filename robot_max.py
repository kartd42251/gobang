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


def eva3(array2D,size): 
    eva_result = [[0 for _ in range(size)] for _ in range(size)]
    _max = -1
    i_max = -1
    j_max = -1
    for i in range(0,size):
        for j in range(0,size):
            Sum = 0
            if(array2D[i][j] == '.'):
                eva_result[i][j] = max(eva_attack(Sum,array2D,i,j),eva_defence(Sum,array2D,i,j))
    for i in range(0,size):
        for j in range(0,size):
            print("{0:^3d}".format(eva_result[i][j]), end = "")
        print()
    print()

    for i in range(0,size):
        for j in range(0,size):
            if(eva_result[i][j] > _max):
                _max = eva_result[i][j]
                i_max = i
                j_max = j

    
    return i_max+1,j_max+1

def eva_defence(Sum,array2D,x,y):
    Sum = 0
    if(x<14 and x>0 and y<14 and y>0):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'or y+k==14): 
                if(array2D[x][14]=='X' and y+k==14):
                   Sum += k*(k+1)/2
                elif(k>4) :
                    Sum += k*(k+1)/2 
                else:
                    Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'or x+k ==14):
                if(array2D[14][y]=='X' and x+k==14):
                   Sum += k*(k+1)/2 
                else:
                    Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'or y+k==14 or x+k ==14):
                if(array2D[14][y+k]=='X' and x+k==14):
                   Sum += k*(k+1)/2
                elif(array2D[x+k][14]=='X' and y+k==14):
                   Sum += k*(k+1)/2 
                else:
                    Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'or x+k ==14):
                if(array2D[14][y-k]=='X' and x+k==14):
                   Sum += k*(k+1)/2
                else:
                    Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'or y+k ==14):
                if(array2D[x-k][14]=='X' and y+k==14):
                    Sum += k*(k+1)/2 
                else:
                    Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x][y-k]!='X'): 
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(x== 0 and 0 < y <14):
        for k in range(1,6):
            if(y+k == 14):
                if(array2D[x][y+k]=='X'):
                    Sum += k*(k+1)/2
                else:
                    Sum += k*(k-1)/2
                break
            elif(array2D[x][y+k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):    
            if(array2D[x][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'or y+k==14):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        return int(Sum) 
    if(y == 0 and x>0 and x<14):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(x+k==14):
                if(array2D[x+k][y]=='X'):
                    Sum += k*(k+1)/2
                else:
                    Sum += k*(k-1)/2
                break
            elif(array2D[x+k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'or x+k==14):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'):
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(y == 0 and x ==0):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'):   
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'):
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(y == 0 and x == 14):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'):
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(x== 14 and y == 14):
        for k in range(1,6):
            if(array2D[x][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(x== 0 and y ==14):
        for k in range(1,6):    
            if(array2D[x][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(x==14 and y<14 and y>0):
        for k in range(1,6):
            if(y+k == 14):
                if(array2D[x][y+k]=='X'):
                    Sum += k*(k+1)/2
                else:
                    Sum += k*(k-1)/2
                break
            elif(array2D[x][y+k]!='X'): 
                Sum += k*(k-1)/2
                break
        for k in range(1,6):    
            if(array2D[x][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'or y+k==14):
                Sum += k*(k-1)/2
                break
        return int(Sum)
    if(x<14 and x>0 and y==14):
        for k in range(1,6):    
            if(array2D[x][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(x+k ==14):
                if(array2D[x+k][y]=='X'):
                    Sum += k*(k+1)/2
                else:
                    Sum += k*(k-1)/2 
                break    
            elif(array2D[x+k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'or x+k==14):
                Sum += k*(k-1)/2
                break
        return int(Sum)
                   


    else:
        return  0  


def eva_attack(Sum,array2D,x,y):
    Sum = 0
    if(x<14 and x>0 and y<14 and y>0 ):
        for k in range(1,6):
            if(array2D[x][y+k]!='O'or y+k==14):
                Sum += k*(k-1)/2
            elif(k>4):
                Sum += k*(k+1)/2 
            break
        for k in range(1,6):    
            if(array2D[x][y-k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='O'or x+k==14):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='O'or x+k==14 or y+k==14):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='O'):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='O'or x+k==14):
                Sum += k*(k-1)/2
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='O')or y+k==14:
                Sum += k*(k-1)/2
                break
        return int(Sum)            


    else:
        return  0

