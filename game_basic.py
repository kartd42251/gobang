import platform
import os
from myturtle import *

def print_gamefield(array2D,size, user):
    if platform.system == 'Windows':
        os.system('cls')
    elif platform.system == 'Linux' or 'Darwin':
        os.system('clear')
    status(user)
    for i in range(0, size):
        for j in range(0, size):
            print(array2D[i][j], end=" ")
            if (j == (size - 1)):
                print(" ")

def set_X(array2D,x, y):
    if(array2D[x-1][y-1] == ('X'or'Y')):
        return 1
    elif(array2D[x-1][y-1] == ('.')):
        array2D[x-1][y-1] = "X"
        turtle_set_X(y, x)
        return 0    
            
    
        
      
def set_O(array2D,x, y):
    if(array2D[x-1][y-1] == ('X'or'Y')):
        return 1

    elif(array2D[x-1][y-1] == ('.')):
        array2D[x-1][y-1] = "O"
        turtle_set_O(y, x)
        return 0
        



def check_win(array2D,size):
    for i in range(0, size):
        for j in range(0, size-4):
            if(array2D[i][j] == array2D[i][j+1] == array2D[i][j+2] == array2D[i][j+3] == array2D[i][j+4] == 'X' or
               array2D[i][j] == array2D[i][j+1] == array2D[i][j+2] == array2D[i][j+3] == array2D[i][j+4] == 'O'):
                return 1
    for i in range(0, size-4):
        for j in range(0, size):
            if(array2D[i][j] == array2D[i+1][j] == array2D[i+2][j] == array2D[i+3][j] == array2D[i+4][j] == 'X' or 
               array2D[i][j] == array2D[i+1][j] == array2D[i+2][j] == array2D[i+3][j] == array2D[i+4][j] == 'O'):
                return 1
    for i in range(0, size-4):
        for j in range(0, size-4):
            if(array2D[i][j] == array2D[i+1][j+1] == array2D[i+2][j+2] == array2D[i+3][j+3] == array2D[i+4][j+4] == 'X' or
               array2D[i][j] == array2D[i+1][j+1] == array2D[i+2][j+2] == array2D[i+3][j+3] == array2D[i+4][j+4] == 'O'):
                return 1
    for i in range(0, size-4):
        for j in range(0, size-4):
            if(array2D[i][j+4] == array2D[i+2][j+2] == array2D[i+3][j+1] == array2D[i+4][j] == array2D[i+1][j+3] == 'X' or
               array2D[i][j+4] == array2D[i+2][j+2] == array2D[i+3][j+1] == array2D[i+4][j] == array2D[i+1][j+3] == 'O'):
                return 1




 
                
           

                   

    
    













                 

