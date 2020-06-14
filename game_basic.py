import platform
import os
from myturtle import *

def print_gamefield(array2D,size):
    if platform.system == 'Windows':
        os.system('cls')
    if platform.system == 'Linux' or 'Darwin':
        os.system('clear')
    for i in range(0, size):
        for j in range(0, size):
            print(array2D[i][j], end=" ")
            if (j == (size - 1)):
                print(" ")

def set_X(array2D,x, y):
    if(array2D[x-1][y-1] == ('.')):
        array2D[x-1][y-1] = "X"
        turtle_set_X(y, x)


def set_O(array2D,x, y):
    if(array2D[x-1][y-1] == ('.')):
        array2D[x-1][y-1] = "O"
        turtle_set_O(y, x)


def check_win(array2D,size):
    for i in range(0, size):
        for j in range(0, size-4):
            if(array2D[i][j] == array2D[i][j+1] == array2D[i][j+2] == array2D[i][j+3] == array2D[i][j+4] == ('X' or 'O')):
                return 1
    for i in range(0, size-4):
        for j in range(0, size):
            if(array2D[i][j] == array2D[i+1][j] == array2D[i+2][j] == array2D[i+3][j] == array2D[i+4][j] == ('X' or 'O')):
                return 1
    for i in range(0, size-4):
        for j in range(0, size-4):
            if(array2D[i][j] == array2D[i+1][j+1] == array2D[i+2][j+2] == array2D[i+3][j+3] == array2D[i+4][j+4] == ('X' or 'O')):
                return 1
    for i in range(0, size-4):
        for j in range(0, size-4):
            if(array2D[i][j+4] == array2D[i+2][j+2] == array2D[i+3][j+1] == array2D[i+4][j] == array2D[i+1][j+3] == ('X' or 'O')):
                return 1


def robot(array2D, size, x):
    for i in range(0, size):
        for j in range(0, size-3):
            if(array2D[i][j] == array2D[i][j+1] == array2D[i][j+2] == array2D[i][j+3] == 'X'):
                if(j == 0 and array2D[i][j+4] == '.'):
                    set_O(array2D, i, j+4)
                elif(j == 11 and array2D[i][j-1] == '.'):
                    set_O(array2D, i, j-1)
                elif(j > 0 and j < 11):
                    if(array2D[i][j-1] == 'O' and array2D[i][j+4] == '.'):
                        set_O(array2D, i, j+4)
                    elif(array2D[i][j+4] == 'O' and array2D[i][j-1] == '.'):
                        set_O(array2D, i, j-1)
                    elif(array2D[i][j+4] == '.' and array2D[i][j-1] == '.'):
                        set_O(array2D, i, j-1)
            elif(j < 11):
                if(array2D[i][j] == array2D[i][j+1] == array2D[i][j+2] == array2D[i][j+4] == 'X'):
                    set_O(array2D, i, j+3)
                elif(array2D[i][j] == array2D[i][j+1] == array2D[i][j+3] == array2D[i][j+4] == 'X'):
                    set_O(array2D, i, j+2)
                elif(array2D[i][j] == array2D[i][j+3] == array2D[i][j+2] == array2D[i][j+4] == 'X'):
                    set_O(array2D, i, j+3)
            else:
                x = 0
    if(x == 0):
        for i in range(0, size-3):
            for j in range(0, size):
                if(array2D[i][j] == array2D[i+1][j] == array2D[i+2][j] == array2D[i+3][j] == 'X'):
                    if(i == 0 and array2D[i+4][j] == '.'):
                        set_O(array2D, i+4, j)
                    elif(i == 11 and array2D[i-1][j] == '.'):
                        set_O(array2D, i-1, j)
                    elif(i > 0 and i < 11):
                        if(array2D[i-1][j] == 'O' and array2D[i+4][j] == '.'):
                            set_O(array2D, i+4, j)
                        elif(array2D[i+4][j] == 'O' and array2D[i-1][j] == '.'):
                            set_O(array2D, i-1, j)
                        elif(array2D[i+4][j] == '.' and array2D[i-1][j] == '.'):
                            set_O(array2D, i-1, j)
                elif(i < 11):
                    if(array2D[i][j] == array2D[i+1][j] == array2D[i+2][j] == array2D[i+4][j] == 'X'):
                        set_O(array2D, i+3, j)
                    elif(array2D[i][j] == array2D[i+1][j] == array2D[i+4][j] == array2D[i+3][j] == 'X'):
                        set_O(array2D, i+2, j)
                    elif(array2D[i][j] == array2D[i+4][j] == array2D[i+2][j] == array2D[i+3][j] == 'X'):
                        set_O(array2D, i+2, j)

