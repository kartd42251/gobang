import platform
import os
from myturtle import *

def wall(array2D,size):
    for i in range (size):
        array2D[0][i]='J'
        array2D[16][i]='J'
        array2D[i][0]='J'
        array2D[i][16]='J'
def set_X(array2D,x, y):
    if(array2D[x][y] == ('X'or'Y')):
        return 1
    elif(array2D[x][y] == ('.')):
        array2D[x][y] = "X"
        turtle_set_X(y, x)
        return 0    
            
      
def set_O(array2D,x, y):
    if(array2D[x][y] == ('X'or'Y')):
        return 1

    elif(array2D[x][y] == ('.')):
        array2D[x][y] = "O"
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

def recordWin():
    fn = "./recorder.txt"
    with open(fn,'a+') as fobj: 
        fobj.write("*")
    fobj.close()

def recordTotal():
    fn = "./recorder.txt"
    with open(fn,'a+') as fobj: 
        fobj.write("@")
    fobj.close()

def readWinRate():
    win = total = 0
    fn = "./recorder.txt"
    with open(fn,'r') as fobj: 
        line = fobj.readline()
    fobj.close()
    for ch in line:
        if(ch == '*'):
            win += 1
        elif(ch == '@'):
            total += 1
    if(total == 0):
        return "NA"   
    else:
        return win/total

def file_init():
    fn = "./recorder.txt"
    with open(fn,'a+') as fobj: 
        fobj.write("init")
    fobj.close()
def turtle_win_rate():
    winning_turtle = turtle.Turtle()
    winning_turtle.up()
    winning_turtle.hideturtle()
    winning_turtle.speed(0)
    winning_turtle.goto(310,100)
    winning_turtle.write("WR:"+str(readWinRate()),font = ("Arial", 15, "normal"))