import random 
from game_basic import *

dic = {(4,0):100,(4,1):120,(3,0):70,(3,1):15,(2,0):20,(2,1):2,(1,0):5,(0,0):0,(0,1):0,(1,1):0,}
dic2 = {(4,0):200,(4,1):150,(3,0):90,(3,1):15,(2,0):20,(2,1):2,(1,0):5,(0,0):0,(0,1):0,(1,1):0,}
direction = {0:(1,0),1:(0,1),2:(1,1),3:(1,-1)}
Sum = [0,0,0,0]


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
                eva_result[i][j] = score(array2D,i,j)
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
    # print("best move (",i_max,",",j_max,")")
    
    return i_max,j_max


def score (array2D,x,y):
    Sum = [0,0,0,0]
    four_in_one = [0,0,0,0]
    three_in_one = [0,0,0,0]
    foolproof = [0,0,0,0]
    double_triple =[0,0,0,0]
    score = [0,0]
    if(x<16 and x>0 and y<16 and y>0):
        for k in range(2):
            if(k == 0):
                symbol = "X"
            else:
                symbol = "O"
            for i in range(4):
                for j in range(1,6):
                    (v_x,v_y) = direction.get(i)
                    (v_x2,v_y2) = (-v_x,-v_y)
                    if(array2D[x+j*v_x][y+j*v_y] != symbol):
                        four_in_one [i] += j-1
                        if(array2D[x+j*v_x][y+j*v_y]=='.'): 
                            Sum[i] +=  dic2.get((j-1,0))
                            three_in_one[i] += j-1
                            foolproof[i] += 100
                            double_triple[i] += j-1
                        elif(array2D[x+j*v_x][y+j*v_y]=='J'): 
                            foolproof[i] += j
                        else:
                            Sum[i] += dic2.get((j-1,1))
                            foolproof[i] += j-1
                        break
                for j in range(1,6):   
                    if(array2D[x+j*v_x2][y+j*v_y2] != symbol):
                        four_in_one[i] += j-1
                        if(array2D[x+j*v_x2][y+j*v_y2]=='.'): 
                            Sum[i] +=  dic2.get((j-1,0))
                            three_in_one[i] += j-1
                            foolproof[i] += 100
                            double_triple[i] += j-1
                        elif(array2D[x+j*v_x2][y+j*v_y2]=='J'): 
                            foolproof[i] += j
                        else:
                            Sum[i] += dic2.get((j-1,1))
                            foolproof[i] += j-1   
                        if(four_in_one [i]>=4):
                            Sum[i] = dic2.get((4,1))
                        elif(i == 1 or 3):
                            if(double_triple[i] + double_triple[i-1]>=4):
                                Sum[i] += dic2.get((3,0))
                        elif(three_in_one[i]==3):
                            Sum[i] = dic2.get((3,0))
                        if(foolproof[i] <4):
                            Sum[i] = 0  
                        break
            score[k] = int(Sum[0] +Sum[1] +Sum[2] +Sum[3])
        return max(score[0],score[1])     
    else:
        return 0








