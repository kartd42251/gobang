import random 
import copy
from game_basic import *

dic2 = {(4,0):250,(4,1):150,(3,0):90,(3,1):15,(2,0):20,(2,1):2,(1,0):5,(0,0):0,(0,1):0,(1,1):0,}
direction = {0:(1,0),1:(0,1),2:(1,1),3:(1,-1)}



def random_init(array2D):
    for i in range(30):
        x = random.randint(1,15)
        y = random.randint(1,15)
        set_X(array2D,x,y)
def manual_init(array2D):

  
    set_O(array2D,6,14)
    set_O(array2D,7,13)
    set_O(array2D,4,14)
    set_X(array2D,8,12)

  

def eva3(array2D,size): 
    eva_result = [[-1 for _ in range(size)] for _ in range(size)]
    _max = -1
    random_max=[]
    li =[]
    for i in range(0,size):
        for j in range(0,size):
            if(array2D[i][j] == '.'):
                eva_result[i][j] = score(array2D,i,j)
    for i in range(0,size):
        for j in range(0,size):
            print("{0:^3d}".format(eva_result[i][j]), end = "")
        print()
    print()
    print()
   
    for i in range(0,size):
        for j in range(0,size):
            if(eva_result[i][j] > _max):
                _max = eva_result[i][j]
                random_max=[]
                random_max.append([i,j])
                #print(random_max)
            elif(eva_result[i][j] ==_max):
                random_max.append([i,j])
    li =random_max[random.randint(0,len(random_max)-1)]
    # print(li)
    # print(random_max)
    
    print("best move (",li[0]," ",li[1],")")  
    return li[0],li[1]

def check_if_need_rand(eva_result,size):
    _max = 0
    for i in range(0,size):
        for j in range(0,size):
            if(eva_result[i][j] > _max):
                _max = eva_result[i][j]
    def elem_cnt(eva_result,size,target):
        cnt = 0
        for i in range(0,size):
            for j in range(0,size): 
                if(eva_result[i][j] == target):
                    cnt += 1
        return cnt
    if(elem_cnt(eva_result,size,0)== size**2):
        return True,0
    elif(elem_cnt(eva_result,size,_max)+elem_cnt(eva_result,size,0)==size**2):
        return True,_max

def score (array2D,x,y):
    if(x<16 and x>0 and y<16 and y>0):
        score = [0,0]
        for k in range(2):
            Sum = [0,0,0,0]
            four_in_one = [0,0,0,0]
            three_in_one = [0,0,0,0]
            foolproof = [0,0,0,0]
            double_triple =[0,0,0,0]
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
                            Sum[i] = dic2.get((4,0))
                        elif(double_triple[i] + double_triple[i-1]>=4):
                            if(i == 3 or i == 1):
                                Sum[i] = dic2.get((3,0))
                        elif(three_in_one[i]==3):
                            Sum[i] = dic2.get((3,0))
                        if(foolproof[i] <4):
                            Sum[i] = 0  
                        break

            score[k] = int(Sum[0] +Sum[1] +Sum[2] +Sum[3])
        return max(score[0],score[1])   
    else:
        return -1

def fake_self_learing(array2D,size):
    eva_result = [[-1 for _ in range(size)] for _ in range(size)]
    eva_result_2 =copy.deepcopy(eva_result)
    _min = -1
    min_x = 0
    min_y = 0
    for i in range(0,size):
        for j in range(0,size):
            if(array2D[i][j] == '.'):
                eva_result[i][j] = score(array2D,i,j)
    for i in range(0,size):
        for j in range(0,size):
            print("{0:^3d}".format(eva_result[i][j]), end = "")
        print()
    print()
    print()
    for k in range(0,size):
        for l in range(0,size):
            if(eva_result[k][l] >0):
                print(k,l)
                array2D_2 = copy.deepcopy(array2D)
                array2D_2[k][l] = "O"
                _max = -1
                for i in range(0,size):
                    for j in range(0,size):
                        if(array2D_2[i][j] == '.'):
                            eva_result_2[i][j] = score(array2D_2,i,j)
                            if(eva_result_2[i][j] > _max):
                                _max = eva_result[i][j]
                if(eva_result[k][l] - _max > _min):
                    _min = eva_result[k][l]
                    print(_min)
                    min_x = k
                    min_y = l
    for i in range(0,size):
        for j in range(0,size):
            print("{0:^3d}".format(eva_result[i][j]), end = "")
        print()
    print()
    print(min_x,min_y)
    return min_x,min_y

                    
     
  








