import random 
from game_basic import *
dic = {(4,0):100,(4,1):90,(3,0):70,(3,1):15,(2,0):20,(2,1):0,(1,0):5,(0,0):0,(0,1):0,(1,1):0}

def random_init(array2D):
    for i in range(30):
        x = random.randint(1,15)
        y = random.randint(1,15)
        set_X(array2D,x,y)
def manual_init(array2D):
    set_X(array2D,4,5)
    set_X(array2D,5,5)
    set_X(array2D,7,5)
    set_X(array2D,8,5)
    set_O(array2D,3,5)
    set_O(array2D,9,5)
    set_X(array2D,5,6)
    set_X(array2D,5,4)
    set_O(array2D,7,4)


def eva3(array2D,size): 
    eva_result = [[0 for _ in range(size)] for _ in range(size)]
    _max = -1
    i_max = -1
    j_max = -1
    for i in range(0,size):
        for j in range(0,size):
            Sum = 0
            if(array2D[i][j] == '.'):
                eva_result[i][j] = (eva_attack(Sum,array2D,i,j)+eva_defence(Sum,array2D,i,j))
    for i in range(0,size):
        for j in range(0,size):
            print("{0:^3d}".format(eva_result[i][j]), end = "")
        print()
    for i in range(0,size):
        for j in range(0,size):
            if(eva_result[i][j] > _max):
                _max = eva_result[i][j]
                i_max = i
                j_max = j
    print("best move (",i_max,",",j_max,")")
    
    return i_max,j_max

def eva_defence(Sum,array2D,x,y):
    Sum_h = 0
    Sum_a = 0 
    Sum_l = 0
    Sum_r = 0
    if(x<16 and x>0 and y<16 and y>0):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'): 
                if(array2D[x][y+k]=='.'): 
                    Sum_h +=  dic.get((k-1,0))
                else:
                    Sum_h += dic.get((k-1,1))   
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'): 
                if(array2D[x+k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                else:
                    Sum_a += dic.get((k-1,1))     
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'): 
                if(array2D[x-k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                else:
                    Sum_a += dic.get((k-1,1))      
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'): 
                if(array2D[x+k][y+k]=='.'): 
                    Sum_l += dic.get((k-1,0))
                else:
                    Sum_l += dic.get((k-1,1))     
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'): 
                if(array2D[x-k][y-k]=='.'): 
                    Sum_l += dic.get((k-1,0))
                else:
                    Sum_l += dic.get((k-1,1))    
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'): 
                if(array2D[x+k][y-k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                else:
                    Sum_r += dic.get((k-1,1))     
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'): 
                if(array2D[x-k][y+k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                else:
                    Sum_r += dic.get((k-1,1))   
                break
        for k in range(1,6): 
            if(array2D[x][y-k]!='X'): 
                if(array2D[x][y-k]=='.'): 
                    Sum_h += dic.get((k-1,0))
                else:
                    Sum_h += dic.get((k-1,1))     
                break
        return int(Sum_h + Sum_a +Sum_l +Sum_r)
    else:
        return 0

    
def eva_attack(Sum,array2D,x,y):
    Sum_h = 0
    Sum_a = 0 
    Sum_l = 0
    Sum_r = 0
    if(x<16 and x>0 and y<16 and y>0):
        for k in range(1,6):
            if(array2D[x][y+k]!='O'): 
                if(array2D[x][y+k]=='.'): 
                    Sum_h +=  dic.get((k-1,0))
                else:
                    Sum_h += dic.get((k-1,1))   
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='O'): 
                if(array2D[x+k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                else:
                    Sum_a += dic.get((k-1,1))     
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='O'): 
                if(array2D[x-k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                else:
                    Sum_a += dic.get((k-1,1))      
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='O'): 
                if(array2D[x+k][y+k]=='.'): 
                    Sum_l += dic.get((k-1,0))
                else:
                    Sum_l += dic.get((k-1,1))     
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='O'): 
                if(array2D[x-k][y-k]=='.'): 
                    Sum_l += dic.get((k-1,0))
                    Sum_l += dic.get((k-1,1))    
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='O'): 
                if(array2D[x+k][y-k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                else:
                    Sum_r += dic.get((k-1,1))     
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='O'): 
                if(array2D[x-k][y+k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                else:
                    Sum_r += dic.get((k-1,1))   
                break
        for k in range(1,6): 
            if(array2D[x][y-k]!='O'): 
                if(array2D[x][y-k]=='.'): 
                    Sum_h += dic.get((k-1,0))
                else:
                    Sum_h += dic.get((k-1,1))     
                break
        return int(Sum_h + Sum_a +Sum_l +Sum_r)
    else:
        return 0