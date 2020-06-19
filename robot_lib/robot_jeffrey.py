import random 
from game_basic import *
dic = {(4,0):100,(4,1):100,(3,0):70,(3,1):4,(2,0):20,(2,1):2,(1,0):5,(0,0):0,(0,1):0,(1,1):0,}
dic2 = {(4,0):200,(4,1):150,(3,0):70,(3,1):15,(2,0):20,(2,1):2,(1,0):5,(0,0):0,(0,1):0,(1,1):0,}

def random_init(array2D):
    for i in range(30):
        x = random.randint(1,15)
        y = random.randint(1,15)
        set_X(array2D,x,y)
def manual_init(array2D):

    set_O(array2D,2,5)
    set_O(array2D,3,5)
    set_O(array2D,4,5)
    set_O(array2D,5,5)
    set_X(array2D,6,5)

  

def eva3(array2D,size): 
    eva_result = [[0 for _ in range(size)] for _ in range(size)]
    _max = -1
    i_max = -1
    j_max = -1
    for i in range(0,size):
        for j in range(0,size):
            if(array2D[i][j] == '.'):
                eva_result[i][j] =  max(eva_defence(array2D,i,j),eva_attack(array2D,i,j))
    # for i in range(0,size):
    #     for j in range(0,size):
    #         print("{0:^3d}".format(eva_result[i][j]), end = "")
    #     print()
    for i in range(0,size):
        for j in range(0,size):
            if(eva_result[i][j] > _max):
                _max = eva_result[i][j]
                i_max = i
                j_max = j
    # print("best move (",i_max,",",j_max,")")
    
    return i_max,j_max

def eva_attack(array2D,x,y):
    Sum_h = 0
    Sum_a = 0 
    Sum_l = 0
    Sum_r = 0
    ct_h = ct_a = ct_l = ct_r = 0
    cnt_h = cnt_a = cnt_l =cnt_r = 0
    stupid_h = stupid_a = stupid_l = stupid_r = 0
    
    if(x<16 and x>0 and y<16 and y>0):
        for k in range(1,6):
            if(array2D[x][y+k]!='O'):
                ct_h += k-1
                if(array2D[x][y+k]=='.'): 
                    Sum_h +=  dic.get((k-1,0))
                    cnt_h += k-1
                    stupid_h += 100
                elif(array2D[x][y+k]=='J'): 
                    stupid_h += k
                else:
                    Sum_h += dic.get((k-1,1))
                    stupid_h += k-1   
                break
        for k in range(1,6): 
            if(array2D[x][y-k]!='O'): 
                ct_h += k-1
                if(array2D[x][y-k]=='.'): 
                    Sum_h += dic.get((k-1,0))
                    cnt_h += k-1
                    stupid_h += 100
                elif(array2D[x][y-k]=='J'): 
                    stupid_h += k
                else:
                    Sum_h += dic.get((k-1,1))
                    stupid_h += k-1 
                if(ct_h>=4):
                    Sum_h = dic.get((4,1))
                elif(cnt_h==3):
                    Sum_h = dic.get((3,0))
                if(stupid_h <5):
                    Sum_h = 0
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='O'): 
                ct_a += k-1
                if(array2D[x+k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                    cnt_a += k-1
                    stupid_a += 100
                elif(array2D[x+k][y]=='J'): 
                    stupid_a += k 
                else:
                    Sum_a += dic.get((k-1,1)) 
                    stupid_a += k-1    
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='O'): 
                ct_a += k-1
                if(array2D[x-k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                    cnt_a += k-1
                    stupid_a += 100
                elif(array2D[x-k][y]=='J'): 
                    stupid_a += k 
                else:
                    Sum_a += dic.get((k-1,1))
                    stupid_a += k-1 
                if(ct_a>=4):
                    Sum_a = dic.get((4,1)) 
                elif(cnt_a==3):
                    Sum_a = dic.get((3,0))    
                if(stupid_a<5):
                    Sum_a = 0  
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='O'): 
                if(array2D[x+k][y+k]=='.'):
                    ct_l += k-1 
                    Sum_l += dic.get((k-1,0))
                    stupid_l += 100
                elif(array2D[x+k][y+k]=='J'):
                    stupid_l += k
                else:
                    Sum_l += dic.get((k-1,1)) 
                    stupid_l += k-1     
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='O'):
                ct_l += k-1 
                if(array2D[x-k][y-k]=='.'): 
                    Sum_l += dic.get((k-1,0))
                    cnt_l += k-1
                    stupid_l += 100
                elif(array2D[x-k][y-k]=='J'):
                    stupid_l += k
                else:
                    Sum_l += dic.get((k-1,1))
                    stupid_l += k-1 
                if(ct_l>=4):
                    Sum_l = dic.get((4,1))   
                elif(cnt_l==3):
                    Sum_l = dic.get((3,0)) 
                if(stupid_l<5):
                    Sum_l = 0 
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='O'):
                ct_r += k-1 
                if(array2D[x+k][y-k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                    cnt_r += k-1
                    stupid_r += 100
                elif(array2D[x+k][y-k]=='J'):
                    stupid_r += k  
                else:
                    Sum_r += dic.get((k-1,1))  
                    stupid_r += k-1   
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='O'): 
                ct_r += k-1
                if(array2D[x-k][y+k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                    cnt_r += k-1
                    stupid_r += 100
                elif(array2D[x-k][y+k]=='J'):
                    stupid_r += k 
                else:
                    Sum_r += dic.get((k-1,1))
                    stupid_r += k-1   
                if(ct_r>=4):
                    Sum_r = dic.get((4,1))
                elif(cnt_r==3):
                    Sum_r = dic.get((3,0))
                    if(stupid_r<5):
                        Sum_r = 0
                break
        
        return int(Sum_h + Sum_a +Sum_l +Sum_r)
    else:
        return 0
def eva_defence(array2D,x,y):
    Sum_h = 0
    Sum_a = 0 
    Sum_l = 0
    Sum_r = 0
    ct_h = ct_a = ct_l = ct_r = 0
    cnt_h = cnt_a = cnt_l =cnt_r = 0
    stupid_h = stupid_a = stupid_l = stupid_r = 0
    
    if(x<16 and x>0 and y<16 and y>0):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'):
                ct_h += k-1
                if(array2D[x][y+k]=='.'): 
                    Sum_h +=  dic.get((k-1,0))
                    cnt_h += k-1
                    stupid_h += 100
                elif(array2D[x][y+k]=='J'): 
                    stupid_h += k
                else:
                    Sum_h += dic.get((k-1,1))
                    stupid_h += k-1   
                break
        for k in range(1,6): 
            if(array2D[x][y-k]!='X'): 
                ct_h += k-1
                if(array2D[x][y-k]=='.'): 
                    Sum_h += dic.get((k-1,0))
                    cnt_h += k-1
                    stupid_h += 100
                elif(array2D[x][y-k]=='J'): 
                    stupid_h += k
                else:
                    Sum_h += dic.get((k-1,1))
                    stupid_h += k-1 
                if(ct_h>=4):
                    Sum_h = dic.get((4,1))
                elif(cnt_h==3):
                    Sum_h = dic.get((3,0))
                if(stupid_h <5):
                    Sum_h = 0
                break
        for k in range(1,6):
            if(array2D[x+k][y]!='X'): 
                ct_a += k-1
                if(array2D[x+k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                    cnt_a += k-1
                    stupid_a += 100
                elif(array2D[x+k][y]=='J'): 
                    stupid_a += k 
                else:
                    Sum_a += dic.get((k-1,1)) 
                    stupid_a += k-1    
                break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'): 
                ct_a += k-1
                if(array2D[x-k][y]=='.'): 
                    Sum_a += dic.get((k-1,0))
                    cnt_a += k-1
                    stupid_a += 100
                elif(array2D[x-k][y]=='J'): 
                    stupid_a += k 
                else:
                    Sum_a += dic.get((k-1,1))
                    stupid_a += k-1 
                if(ct_a>=4):
                    Sum_a = dic.get((4,1)) 
                elif(cnt_a==3):
                    Sum_a = dic.get((3,0))    
                if(stupid_a<5):
                    Sum_a = 0  
                break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'):
                ct_l += k-1 
                if(array2D[x+k][y+k]=='.'):
                    Sum_l += dic.get((k-1,0))
                    stupid_l += 100
                elif(array2D[x+k][y+k]=='J'):
                    stupid_l += k
                else:
                    Sum_l += dic.get((k-1,1)) 
                    stupid_l += k-1     
                break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                ct_l += k-1 
                if(array2D[x-k][y-k]=='.'): 
                    Sum_l += dic.get((k-1,0))
                    cnt_l += k-1
                    stupid_l += 100
                elif(array2D[x-k][y-k]=='J'):
                    stupid_l += k
                else:
                    Sum_l += dic.get((k-1,1))
                    stupid_l += k-1 
                if(ct_l>=4):
                    Sum_l = dic.get((4,1))   
                elif(cnt_l==3):
                    Sum_l = dic.get((3,0)) 
                if(stupid_l<5):
                    Sum_l = 0 
                break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'):
                ct_r += k-1 
                if(array2D[x+k][y-k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                    cnt_r += k-1
                    stupid_r += 100
                elif(array2D[x+k][y-k]=='J'):
                    stupid_r += k  
                else:
                    Sum_r += dic.get((k-1,1))  
                    stupid_r += k-1   
                break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'): 
                ct_r += k-1
                if(array2D[x-k][y+k]=='.'): 
                    Sum_r += dic.get((k-1,0))
                    cnt_r += k-1
                    stupid_r += 100
                elif(array2D[x-k][y+k]=='J'):
                    stupid_r += k 
                else:
                    Sum_r += dic.get((k-1,1))
                    stupid_r += k-1   
                if(ct_r>=4):
                    Sum_r = dic.get((4,1))
                elif(cnt_r==3):
                    Sum_r = dic.get((3,0))
                    if(stupid_r<5):
                        Sum_r = 0
                break
        
        return int(Sum_h + Sum_a +Sum_l +Sum_r)
    else:
        return 0