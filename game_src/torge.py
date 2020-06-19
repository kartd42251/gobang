import sys
sys.path.insert(1, '../game_lib')
sys.path.insert(1, '../robot_lib')

import torge_turtle 
from game_basic import *
from robot_jeffrey import *
import time

x = 0
y = 0
x_temp = 8
y_temp = 8
print("W!!!!!!!!!!!!!!!!!")
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
    
def key_detect(turtle):
    turtle.listen()
    turtle.onkeypress(x_plus,"Right")
    turtle.onkeypress(x_mius,"Left")
    turtle.onkeypress(y_plus,"Down")
    turtle.onkeypress(y_mius,"Up")
    turtle.onkeypress(enter,"space")

def main():
    mode = -1 # 0 for pvp, 1 for pvc
    
    writer = turtle.Turtle()
    arrow = turtle.Turtle()
    comp_m = turtle.Turtle()


    turtle_init() 
    arrow_init(arrow)
    writer_init(writer)
    file_init()
    torge_turtle.comp_mouse_init(comp_m)

    turtle_gamefield()
    turtle_win_rate()
    shutdown = 0
    size = 17
    user = 1 # 1 for x -1 for y
    array2D = [['.' for _ in range(size)] for _ in range(size)]
    for i in range (size):
        array2D[0][i]='J'
        array2D[16][i]='J'
        array2D[i][0]='J'
        array2D[i][16]='J'

    if_same_spot = -1
    #manual_init(array2D)
    mode = int(turtle.numinput("Choose Mode","0 for pvp and 1 for pvc",1,0,1))
    if(mode == 1):
        first_hand = turtle.textinput("First hand?","First hand?(y/n)")
    if(mode == 0):
        first_hand = 'n'

    if(first_hand == 'n'):
        set_O(array2D,8,8)
    key_detect(turtle)
    torge_turtle.choice_character()
    while(not shutdown):
        arrow.goto((-13.4+2*(x_temp-1))*t_size, (14-2*(y_temp-1))*t_size)  
        turtle.update()
        global x, y
        if(user == 1 and x > 0):
            if_same_spot = set_X(array2D, y, x)
        if(mode == 0 and user == -1 and y > 0):
            if_same_spot = set_O(array2D, y, x)
        if(mode == 1 and user == -1 and y > 0):
            y, x = eva3(array2D,size)
            set_O(array2D, y, x)    
            torge_turtle.comp_mouse_move(comp_m,x,y)
        if(check_win(array2D, size) == 1):
            shutdown = 1
            writer.clear()
            if(user == 1):
                turtle_check_win(size,"User",writer)
                recordWin()
            elif(user == -1):
                turtle_check_win(size,"Comp",writer)
            torge_turtle.ending_surprise(user)
        else:
            if(if_same_spot == 0 ):
                user *= -1
                status(writer,user)

    
    turtle.done()
    if(mode == 1):
        recordTotal()    
        print("WINNING RATE:",readWinRate())
if __name__ == "__main__":
    main()