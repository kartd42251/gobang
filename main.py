import platform
import os
import turtle
def turtle_init():
    turtle.width(3)
    turtle.hideturtle()
def draw_square():
    for _ in range(4):
        turtle.forward(30*t_size)
        turtle.right(90)
def draw_line():
    for i in range(15):
        turtle.right(90)
        turtle.forward(2*t_size)
        turtle.left(90)
        turtle.forward(30*t_size)
        turtle.backward(30*t_size)
def turtle_gamefield():
    turtle.tracer(False)
    turtle_init()
    turtle.up()
    turtle.goto(-15*t_size,15*t_size)
    turtle.down()
    draw_square()
    draw_line()
    turtle.left(90)
    draw_line()
    turtle.tracer(True)
    turtle.up()
t_size = 20
turtle_gamefield()

def turtle_set_X(x,y):
    turtle.goto((-14+2*(x-1))*t_size-t_size/4,(14-2*(y-1))*t_size-t_size/2)
    turtle.write('X',font=("Arial", 20, "normal"))
def turtle_set_O(x,y):
    turtle.goto((-14+2*(x-1))*t_size-t_size/4,(14-2*(y-1))*t_size-t_size/2)
    turtle.write('O',font=("Arial", 20, "normal"))
    print("OOOOO")
def print_gamefield(size):
    if platform.system == 'Windows':
        os.system('cls')
    if platform.system == 'Linux' or 'Darwin':
        os.system('clear')
    for i in range(0,size):
        for j in range(0,size):
            print(array2D[i][j],end=" ")
            if (j == (size -1)):
                print(" ")
               
def set_X(x,y):
    if(array2D[x-1][y-1] == ('.')):
        array2D[x-1][y-1] = "X" 
        turtle_set_X(y,x)
def set_O(x,y):
    if(array2D[x-1][y-1] == ('.')):
        array2D[x-1][y-1] = "O"
        turtle_set_O(y,x)

def check_win(size):
    for i in range(0,size):
        for j in range(0,size-4):
            if(array2D[i][j]==array2D[i][j+1]==array2D[i][j+2]==array2D[i][j+3]==array2D[i][j+4]==('X'or'O')):                
                return 1
    for i in range(0,size-4):
        for j in range(0,size):
            if(array2D[i][j]==array2D[i+1][j]==array2D[i+2][j]==array2D[i+3][j]==array2D[i+4][j]==('X'or'O')):
                return  1
    for i in range(0,size-4):
        for j in range(0,size-4):        
            if(array2D[i][j]==array2D[i+1][j+1]==array2D[i+2][j+2]==array2D[i+3][j+3]==array2D[i+4][j+4]==('X'or'O')):
                return  1
    for i in range(0,size-4):
        for j in range(0,size-4):                
            if(array2D[i][j+4]==array2D[i+2][j+2]==array2D[i+3][j+1]==array2D[i+4][j]==array2D[i+1][j+3]==('X'or'O')):
                return  1
def robot(size,x):
    for i in range(0,size):
        for j in range(0,size-3):
            if(array2D[i][j]==array2D[i][j+1]==array2D[i][j+2]==array2D[i][j+3]=='X'):                
                if(j == 0 and array2D[i][j+4] == '.' ):
                    set_O(i,j+4)
                elif(j == 11 and array2D[i][j-1] == '.' ):
                    set_O(i,j-1) 
                elif(j > 0 and j <11):
                    if(array2D[i][j-1] == 'O' and array2D[i][j+4] == '.' ):
                        set_O(i,j+4) 
                    elif(array2D[i][j+4] == 'O' and array2D[i][j-1] == '.' ):
                        set_O(i,j-1)
                    elif(array2D[i][j+4] == '.' and array2D[i][j-1] == '.' ):
                        set_O(i,j-1)    
            elif(j<11):
                if(array2D[i][j]==array2D[i][j+1]==array2D[i][j+2]==array2D[i][j+4]=='X'):                
                    set_O(i,j+3)
                elif(array2D[i][j]==array2D[i][j+1]==array2D[i][j+3]==array2D[i][j+4]=='X'):                
                    set_O(i,j+2) 
                elif(array2D[i][j]==array2D[i][j+3]==array2D[i][j+2]==array2D[i][j+4]=='X'):                
                    set_O(i,j+3) 
            else:
                x = 0
    if(x == 0):
        for i in range(0,size-3):
            for j in range(0,size):
                if(array2D[i][j]==array2D[i+1][j]==array2D[i+2][j]==array2D[i+3][j]=='X'):                
                    if(i == 0 and array2D[i+4][j] == '.' ):
                        set_O(i+4,j)
                    elif(i == 11 and array2D[i-1][j] == '.' ):
                        set_O(i-1,j)  
                    elif(i > 0 and i <11):
                        if(array2D[i-1][j] == 'O' and array2D[i+4][j] == '.' ):
                            set_O(i+4,j)
                        elif(array2D[i+4][j] == 'O' and array2D[i-1][j] == '.' ):
                            set_O(i-1,j) 
                        elif(array2D[i+4][j] == '.' and array2D[i-1][j] == '.' ):
                            set_O(i-1,j)    
                elif(i<11):
                    if(array2D[i][j]==array2D[i+1][j]==array2D[i+2][j]==array2D[i+4][j]=='X'):                
                        set_O(i+3,j)  
                    elif(array2D[i][j]==array2D[i+1][j]==array2D[i+4][j]==array2D[i+3][j]=='X'):                
                        set_O(i+2,j) 
                    elif(array2D[i][j]==array2D[i+4][j]==array2D[i+2][j]==array2D[i+3][j]=='X'):              
                        set_O(i+2,j)  
                
                

                   

    
    







shutdown = 0
size = 15
array2D = [["." for _ in range(size)] for _ in range(size)]        
while shutdown ==0:
    x = 1
    print_gamefield(size) 
    print("X turn")
    x = int(input("x-axis: ")) 
    y = int(input("y-axis: "))
    set_X(y,x)
    
    if(check_win(size) == 1):
        shutdown = 1
        print_gamefield(size)
        print('X win')
        
    else:
        print_gamefield(size) 
        robot(size,x)
        if(check_win(size) == 1):
            shutdown = 1
            print_gamefield(size)
            print('O win')
    
