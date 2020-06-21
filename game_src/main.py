import sys
sys.path.insert(1, '../game_lib')
sys.path.insert(1, '../robot_lib')

from myturtle import *
from game_basic import *
from robot_jeffrey import *
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
    user_arrow = turtle.Turtle()
    comp_arrow = turtle.Turtle()

    turtle_init() 
    writer_init(writer)
    file_init()
    comp_mouse_init(comp_arrow)
    arrow_init(user_arrow)

    turtle_gamefield()
    turtle_win_rate()

    shutdown = 0
    size = 17
    user = 1 # 1 for x -1 for y
    array2D = [['.' for _ in range(size)] for _ in range(size)]
    wall(array2D,size)
    if_same_spot = -1
    #manual_init(array2D)
    first_hand = 'NA'

    mode = int(turtle.numinput("Choose Mode","0 for pvp and 1 for pvc",2,0,2))
    if(mode == 1):
        first_hand = turtle.textinput("First hand?","First hand?(y/n)")
    if(mode == 2 ):
        first_hand = 'n'
    
    if(first_hand == 'n'):
        set_O(array2D,8,8)
        
    key_detect(turtle)
    #choice_character()
    while(not shutdown):
        turtle.update()
        global x, y, temp_x, temp_y

        if(mode == 0):
            if(user == 1):
                if_same_spot = set_X(array2D, y, x)
                mouse_move(user_arrow,x_temp,y_temp) 
            if(user == -1):
                if_same_spot = set_O(array2D, y, x)
                mouse_move(comp_arrow,x_temp,y_temp) 
        if(mode == 1):
            if(user == 1 ):
                mouse_move(user_arrow,x_temp,y_temp)
                if_same_spot = set_X(array2D, y, x)
            if(user == -1):
                y, x = fake_self_learing(array2D,size)
                set_O(array2D, y, x)    
                mouse_move(comp_arrow,x,y)
        if(mode == 2):
            if(user == 1):
                y, x = fake_self_learing(array2D,size)
                if_same_spot = set_X(array2D, y, x) 
                mouse_move(user_arrow,x,y)
            if(user == -1):
                y, x = eva3(array2D,size)
                if_same_spot = set_O(array2D, y, x)    
                mouse_move(comp_arrow,x,y)  

        if(check_win(array2D, size) == 1):
            shutdown = 1
            writer.clear()
            if(user == 1):
                turtle_check_win(size,"User",writer)
                recordWin()
            elif(user == -1):
                turtle_check_win(size,"Comp",writer)
            #ending_surprise(user)
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