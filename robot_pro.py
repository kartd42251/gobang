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

def eva_defence(Sum,array2D,x,y):
    Sum = 0
    if(x<12 and x>2 and y<12 and y>2 ):
        for k in range(1,6):
            if(array2D[x][y+k]!='X'):
                if(array2D[x][y+k]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        for k in range(1,6):    
            if(array2D[x][y-k]!='X'):
                if(array2D[x][y-k]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
                
        for k in range(1,6):
            if(array2D[x+k][y]!='X'):
                if(array2D[x+k][y]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        for k in range(1,6):        
            if(array2D[x-k][y]!='X'):
                if(array2D[x-k][y]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        for k in range(1,6):        
            if(array2D[x+k][y+k]!='X'):
                if(array2D[x+k][y+k]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        for k in range(1,6):        
            if(array2D[x-k][y-k]!='X'):
                if(array2D[x-k][y-k]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        for k in range(1,6):        
            if(array2D[x+k][y-k]!='X'):
                if(array2D[x+k][y-k]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        for k in range(1,6):        
            if(array2D[x-k][y+k]!='X'):
                if(array2D[x-k][y+k]=='.'):
                    Sum += k*(k+1)/2
                    break
                else:
                    Sum += k*(k-1)/2
                    break
        return Sum            


    else:
        return  0  


def eva_attack(Sum,array2D,x,y):
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