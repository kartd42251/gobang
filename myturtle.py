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
    turtle.goto(-15*t_size, 15*t_size)
    turtle.down()
    draw_square()
    draw_line()
    turtle.left(90)
    draw_line()
    turtle.tracer(True)
    turtle.up()


t_size = 20

def turtle_set_X(x, y):
    turtle.goto((-14+2*(x-1))*t_size-t_size/4, (14-2*(y-1))*t_size-t_size/2)
    turtle.write('X', font=("Arial", 20, "normal"))


def turtle_set_O(x, y):
    turtle.goto((-14+2*(x-1))*t_size-t_size/4, (14-2*(y-1))*t_size-t_size/2)
    turtle.write('O', font=("Arial", 20, "normal"))

def turtle_check_win(size):
    turtle.goto(0,t_size*size+20)
    turtle.write('Player win', align="center",font=("Arial", 40, "normal"))


