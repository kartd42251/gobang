import turtle
import random

def turtle_init():
    turtle.right(90)
    turtle.setup(800,600)
    turtle.screensize(3000,3000)
    turtle.setworldcoordinates(-400,-400,400,400)
    turtle.width(3)
    turtle.hideturtle()
    turtle.tracer(False)
    
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

def draw_number():
    turtle.tracer(False)
    turtle.up()
    turtle.goto(-14*t_size, 15.2*t_size)
    for i in range(15):
        turtle.write(i+1, font=("Arial", 15, "normal"))
        turtle.forward(2*t_size)
    turtle.goto(-16*t_size, 13.5*t_size)
    turtle.right(90)
    for i in range(15):
        turtle.write(i+1, font=("Arial", 15, "normal"))
        turtle.forward(2*t_size)
    turtle.left(90)

def turtle_gamefield():
    turtle.tracer(False)
    pos_x, pos_y = turtle.pos()
    draw_number()
    turtle.goto(pos_x,pos_y)
    turtle.up()
    turtle.goto(-15*t_size, 15*t_size)
    turtle.down()
    draw_square()
    draw_line()
    turtle.left(90)
    draw_line()
    turtle.tracer(True)
    turtle.up()
    turtle.right(90)

t_size = 20
def turtle_set_X(x, y):
    turtle.goto((-14.2+2*(x-1))*t_size-t_size/4, (13.5-2*(y-1))*t_size-t_size/2)
    turtle.write('X', font=("Arial", 20, "normal"))


def turtle_set_O(x, y):
    turtle.goto((-14.2+2*(x-1))*t_size-t_size/4, (13.5-2*(y-1))*t_size-t_size/2)
    turtle.write('O', font=("Arial", 20, "normal"))

def turtle_check_win(size,str,writer):
    writer.clear()
    turtle.goto(0,t_size*size)
    turtle.write(str+' win', align="center",font=("Arial", 30, "normal"))

#arrow
def arrow_init(arrow):
    arrow.up()
    arrow.left(90)

#writer
def writer_init(writer):
    writer.hideturtle()
    writer.speed(0)

last_user = -2
def status(writer,user):
    writer.up()
    writer.goto(0,350)
    writer.down()
    global last_user
    if(user != last_user):
        writer.clear()
        if(user == 1):
            writer.write("now is Jason's turn", align="center", font=("Arial", 20, "normal"))
        if(user == -1):
            writer.write("now is Jeffery's turn", align="center", font=("Arial", 20, "normal"))
        last_user = user

def choice_character():
    def process(x,y):
        if(-290 <= x <= -110 ):
            img = IMG[0]
            img.goto(-370,0)
            IMG[1].hideturtle() 
            IMG[2].hideturtle() 
        elif(-90 <= x <= 90):
            img = IMG[1]
            img.goto(-370,0)
            IMG[0].hideturtle()
            IMG[2].hideturtle() 
        elif( 110 <= x <= 290 ):
            img = IMG[2]
            img.goto(-370,0)
            IMG[0].hideturtle()
            IMG[1].hideturtle() 
        jef = turtle.Turtle()
        jef.up()
        turtle.addshape("./img0.gif")
        jef.shape("./img0.gif")
        jef.goto(350,0)
        return

    IMG = [0]*3
    randList = [2,3,4,5,6,7,8,9,10]
    rand_index = random.sample(randList,3)       

    for i in range(3):
        
        IMG[i] = turtle.Turtle()
        turtle.addshape("./img"+str(rand_index[i])+".gif") 
        IMG[i].shape("./img"+str(rand_index[i])+".gif")  
        IMG[i].up()
        IMG[i].goto(200*(i-1),0)
        IMG[i].onclick(process)


def ending_surprise(user):
    turtle.addshape("./img21.gif") 
    turtle.addshape("./img22.gif") 
    ending_turtle = turtle.Turtle()
    ending_writer = turtle.Turtle()
    ending_writer.up()
    ending_writer.hideturtle()
    ending_writer.goto(0,-370)
    if(user == 1):
        ending_turtle.shape("./img21.gif")
        ending_writer.write("你就棒", align="center", font=("Arial", 50, "normal"))
    elif(user == -1):
        ending_turtle.shape("./img22.gif")
        ending_writer.write("吳隆傑又在使", align="center", font=("Arial", 50, "normal"))
    def ending_clear(x,y):
        ending_turtle.hideturtle()
    ending_turtle.onclick(ending_clear)

def comp_mouse_init(comp_m):
    comp_m.speed(0)
    comp_m.up()
    comp_m.color("red")
    comp_m.left(90)
    
def comp_mouse_move(comp_m,x,y):
    comp_m.goto((-13.4+2*(x-1))*t_size, (14-2*(y-1))*t_size)  
