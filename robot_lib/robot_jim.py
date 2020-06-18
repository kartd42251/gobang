import random 
from game_basic import *
dic = {(4,0):1000,(4,1):900,(3,0):70,(3,1):15,(2,0):20,(2,1):0,(1,0):5,(0,0):0,(0,1):0,(1,1):0}
dic2 = {(4,0):10000,(4,1):900,(3,0):70,(3,1):15,(2,0):20,(2,1):0,(1,0):5,(0,0):0,(0,1):0,(1,1):0}

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

def SSD_eva_def(array2D,head_point,vector):
    cross_num = 0
    is_dead = 0
    new_head_point = [0,0]
    new_head_point[0] = head_point[0] 
    new_head_point[1] = head_point[1] 
    for i in range(5):
        new_head_point[0] += vector[0]
        new_head_point[1] += vector[1]
        if(array2D[new_head_point[0]][new_head_point[1]] == '.'):
            break
        if(array2D[new_head_point[0]][new_head_point[1]] == 'O' or array2D[new_head_point[0]][new_head_point[1]] == 'J'):
            is_dead = 1
            break
        if(array2D[new_head_point[0]][new_head_point[1]] == "X"):
            cross_num+=1
        
        if(new_head_point[0] > 16 or new_head_point[0] < 1 or \
           new_head_point[1] > 16 or new_head_point[1] < 1):
            break
    return cross_num, is_dead

def SSD_eva_off(array2D,head_point,vector):
    cross_num = 0
    is_dead = 0
    new_head_point = [0,0]
    new_head_point[0] = head_point[0] 
    new_head_point[1] = head_point[1] 
    for i in range(5):
        new_head_point[0] += vector[0]
        new_head_point[1] += vector[1]
        if(array2D[new_head_point[0]][new_head_point[1]] == '.'):
            break
        if(array2D[new_head_point[0]][new_head_point[1]] == 'X' or array2D[new_head_point[0]][new_head_point[1]] == 'J'):
            is_dead = 1
            break
        if(array2D[new_head_point[0]][new_head_point[1]] == "O"):
            cross_num+=1

        if(new_head_point[0] > 16 or new_head_point[0] < 1 or \
           new_head_point[1] > 16 or new_head_point[1] < 1):
            break
    return cross_num, is_dead

def eva_4(array2D,x,y,mode):
    Sum_h = Sum_a = Sum_l = Sum_r = 0

    if(0 < x < 16 and 0 < y < 16):
        if(mode == "sum"  ):
            Sum_h = dic.get((SSD_eva_def(array2D,(x,y),(1,0)))) + \
                    dic.get((SSD_eva_def(array2D,(x,y),(-1,0))))+ \
                    dic.get((SSD_eva_off(array2D,(x,y),(1,0)))) + \
                    dic.get((SSD_eva_off(array2D,(x,y),(-1,0))))

            Sum_a = dic.get((SSD_eva_def(array2D,(x,y),(0,1)))) +  \
                    dic.get((SSD_eva_def(array2D,(x,y),(0,-1))))+  \
                    dic.get((SSD_eva_off(array2D,(x,y),(0,1)))) +  \
                    dic.get((SSD_eva_off(array2D,(x,y),(0,-1))))

            Sum_l = dic.get((SSD_eva_def(array2D,(x,y),(1,1)))) +  \
                    dic.get((SSD_eva_def(array2D,(x,y),(-1,-1))))+ \
                    dic.get((SSD_eva_off(array2D,(x,y),(1,1)))) +  \
                    dic.get((SSD_eva_off(array2D,(x,y),(-1,-1))))

            Sum_r = dic.get((SSD_eva_def(array2D,(x,y),(1,-1))))+  \
                    dic.get((SSD_eva_def(array2D,(x,y),(-1,1))))+  \
                    dic.get((SSD_eva_off(array2D,(x,y),(1,-1))))+  \
                    dic.get((SSD_eva_off(array2D,(x,y),(-1,1))))
        if(mode == "max"):
            if(SSD_eva_def(array2D,(x,y),(1,0))[0]+SSD_eva_def(array2D,(x,y),(-1,0))[0] >= 4 or\
                SSD_eva_off(array2D,(x,y),(1,0))[0]+SSD_eva_off(array2D,(x,y),(-1,0))[0] >= 4):
                Sum_h = dic.get((4,1))
            else:
                Sum_h = max(dic.get(SSD_eva_def(array2D,(x,y),(1,0))) + \
                    dic.get(SSD_eva_def(array2D,(x,y),(-1,0))),
                    dic2.get(SSD_eva_off(array2D,(x,y),(1,0))) + \
                    dic2.get(SSD_eva_off(array2D,(x,y),(-1,0))))
            if(SSD_eva_def(array2D,(x,y),(0,1))[0]+SSD_eva_def(array2D,(x,y),(0,-1))[0] >= 4 or\
                SSD_eva_off(array2D,(x,y),(0,1))[0]+SSD_eva_off(array2D,(x,y),(0,-1))[0] >= 4):
                Sum_a = dic.get((4,1))
            else:
                Sum_a = max(dic.get(SSD_eva_def(array2D,(x,y),(0,1))) +  \
                    dic.get(SSD_eva_def(array2D,(x,y),(0,-1))),
                    dic2.get(SSD_eva_off(array2D,(x,y),(0,1))) +  \
                    dic2.get(SSD_eva_off(array2D,(x,y),(0,-1))))
            if(SSD_eva_def(array2D,(x,y),(1,1))[0]+SSD_eva_def(array2D,(x,y),(-1,-1))[0] >= 4 or\
                SSD_eva_off(array2D,(x,y),(1,1))[0]+SSD_eva_off(array2D,(x,y),(-1,-1))[0] >= 4):
                Sum_l = dic.get((4,1))
            else:
                Sum_l = max(dic.get(SSD_eva_def(array2D,(x,y),(1,1))) +  \
                    dic.get(SSD_eva_def(array2D,(x,y),(-1,-1))),
                    dic2.get(SSD_eva_off(array2D,(x,y),(1,1))) +  \
                    dic2.get(SSD_eva_off(array2D,(x,y),(-1,-1))))
            if(SSD_eva_def(array2D,(x,y),(1,-1))[0]+SSD_eva_def(array2D,(x,y),(-1,1))[0] >= 4 or\
                SSD_eva_off(array2D,(x,y),(1,-1))[0]+SSD_eva_off(array2D,(x,y),(-1,1))[0] >= 4):
                Sum_r = dic.get((4,1))
            else:
                Sum_r = max(dic.get(SSD_eva_def(array2D,(x,y),(1,-1)))+  \
                    dic.get(SSD_eva_def(array2D,(x,y),(-1,1))),
                    dic2.get(SSD_eva_off(array2D,(x,y),(1,-1)))+  \
                    dic2.get(SSD_eva_off(array2D,(x,y),(-1,1))))

    return Sum_h+Sum_a+Sum_l+Sum_r

def eva3(array2D,size): 
    eva_result = [[0 for _ in range(size)] for _ in range(size)]
    _max = -1
    i_max = -1
    j_max = -1
    for i in range(0,size):
        for j in range(0,size):
            if(array2D[i][j] == '.'):
                eva_result[i][j] = eva_4(array2D,i,j,"max")
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

def eva_defence(array2D,x,y):
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

def eva_attack(array2D,x,y):
    Sum_h = 1
    Sum_a = 1
    Sum_l = 1
    Sum_r = 1
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