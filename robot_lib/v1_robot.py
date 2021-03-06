import random 
from game_basic import *
dic = {(4,0):(100),(4,1):(90),(3,0):70,(3,1):30,(2,0):20,(2,1):0,(1,1):0,(1,0):0,(0,0):0,(0,1):0}

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
                    Sum_h +=  dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_h += dict.fromkeys(dic,(k-1,1))    
            break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'): 
                Sum_a += k*(k+1)/2
                if(array2D[x+k][y]=='.'): 
                    Sum_a += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_a += dict.fromkeys(dic,(k-1,1))    
            break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'): 
                Sum_a+= k*(k+1)/2
                if(array2D[x-k][y]=='.'): 
                    Sum_a += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_a += dict.fromkeys(dic,(k-1,1))   
            break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'): 
                Sum_l += k*(k+1)/2
                if(array2D[x+k][y+k]=='.'): 
                    Sum_l += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_l += dict.fromkeys(dic,(k-1,1))     
            break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'): 
                Sum_l += k*(k+1)/2
                if(array2D[x-k][y-k]=='.'): 
                    Sum_l += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_l += dict.fromkeys(dic,(k-1,1))   
            break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'): 
                Sum_r += k*(k+1)/2
                if(array2D[x+k][y-k]=='.'): 
                    Sum_r += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_r += dict.fromkeys(dic,(k-1,1))     
            break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'): 
                Sum_r += k*(k+1)/2
                if(array2D[x-k][y+k]=='.'): 
                    Sum_r += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_r += dict.fromkeys(dic,(k-1,1))     
            break
        for k in range(1,6): 
            if(array2D[x][y-k]!='X'): 
                Sum_h += k*(k+1)/2
                if(array2D[x][y-k]=='.'): 
                    Sum_h += dict.fromkeys(dic,(k-1,0))
                else:
                    Sum_h += dict.fromkeys(dic,(k-1,1))    
            break
        return int(Sum_h + Sum_a +Sum_l +Sum_r)
    else:
        return 0

    
def eva_attack(Sum,array2D,x,y):
    Sum = 0
   
    return 0





    