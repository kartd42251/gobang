from myturtle import *
from game_basic import *
from robot import *
import time

x = 0
y = 0
x_temp = 8
y_temp = 8

def x_plus():
    global x_temp
    x_temp += 1
    if(x_temp<1):
        x_temp=1
    if(x_temp>15):
        x_temp=15
def x_mius():
    global x_temp
    x_temp -= 1
    if(x_temp<1):
        x_temp=1
    if(x_temp>15):
        x_temp=15
def y_plus():
    global y_temp
    y_temp += 1
    if(y_temp<1):
        y_temp=1
    if(y_temp>15):
        y_temp=15
        
def y_mius():
    global y_temp
    y_temp -= 1
    if(y_temp<1):
        y_temp=1
    if(y_temp>15):
        y_temp=15
        
def enter():
    global x
    global y
    global x_temp
    global y_temp
    x = x_temp
    y = y_temp
    
arrow = turtle.Turtle()

def arrow_init():
    arrow.up()
    arrow.left(90)

def main():
    mode = -1 # 0 for pvp, 1 for pvc
    
    writer = turtle.Turtle()

    turtle_init() 
    turtle_gamefield()
    arrow_init()
    turtle.right(90)
    shutdown = 0
    size = 15
    user = 1 # 1 for x -1 for y
    array2D = [["." for _ in range(size)] for _ in range(size)]
    stupid = 2

    print_gamefield(array2D, size, user,writer)

    mode = int(turtle.numinput("Choose Mode","0 for pvp and 1 for pvc",1,0,1))

    turtle.listen()
    turtle.onkeypress(x_plus,"Right")
    turtle.onkeypress(x_mius,"Left")
    turtle.onkeypress(y_plus,"Down")
    turtle.onkeypress(y_mius,"Up")
    turtle.onkeypress(enter,"space")
    while(not shutdown):
        arrow.goto((-14.2+2*(x_temp-1))*t_size-t_size/4+t_size, (13.5-2*(y_temp-1))*t_size-t_size/2+t_size)  
        turtle.update()
        global x, y
        if(user == 1 and x > 0):
            stupid = set_X(array2D, y, x)
            set_X(array2D, y, x)
        if(mode == 0):
            if(user == -1 and y > 0):
                stupid = set_O(array2D, y, x)
                set_O(array2D, y, x)
        if(mode == 1):
            if(user == -1 and y > 0):
                y, x = eva3(array2D,size)
                set_O(array2D, y, x)    
        
        if(check_win(array2D, size) == 1):
            shutdown = 1
            if(user == 1):
                turtle_check_win(size,"Jason")
            elif(user == -1):
                turtle_check_win(size,"Jeffery")
            
        if(stupid == 0 and check_win(array2D, size)!=1 ):
            user *= -1
            print_gamefield(array2D, size, user, writer)
        
    turtle.done()
        
if __name__ == "__main__":
    main()
    
