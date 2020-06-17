import turtle

def turtle_init():
    turtle.right(90)
    turtle.screensize(1000,1000)
    turtle.setworldcoordinates(-400,-400,400,400)
    turtle.width(3)
    turtle.hideturtle()
    turtle.tracer(False)
    
def draw_square():
    for _ in range(4):
        turtle.forward(30*t_size)
        turtle.right(90)
def arrow_init(arrow):
    arrow.up()
    arrow.left(90)


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


def status(writer,user):
    writer.hideturtle()
    writer.clear()
    writer.speed(0)
    writer.up()
    writer.goto(0,350)
    writer.down()
    if(user == 1):
        writer.write("now is Jason's turn", align="center", font=("Arial", 20, "normal"))
    if(user == -1):
        writer.write("now is Jeffrey's turn", align="center", font=("Arial", 20, "normal"))
def status_clear(writer):
    writer.clear()
t_size = 20

def turtle_set_X(x, y):
    turtle.goto((-14.2+2*(x-1))*t_size-t_size/4, (13.5-2*(y-1))*t_size-t_size/2)
    turtle.write('X', font=("Arial", 20, "normal"))


def turtle_set_O(x, y):
    turtle.goto((-14.2+2*(x-1))*t_size-t_size/4, (13.5-2*(y-1))*t_size-t_size/2)
    turtle.write('O', font=("Arial", 20, "normal"))

def turtle_check_win(size,str,writer):
    status_clear(writer)
    turtle.goto(0,t_size*size+20)
    turtle.write(str+' win', align="center",font=("Arial", 40, "normal"))

