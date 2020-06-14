from myturtle import *
from game_basic import *
turtle_gamefield()
shutdown = 0
size = 15
array2D = [["." for _ in range(size)] for _ in range(size)]
while shutdown == 0:
    x = 1
    print_gamefield(array2D,size)
    print("X turn")
    x = int(turtle.numinput("turtle", "x pos:",default=None, minval=1, maxval=15))
    y = int(turtle.numinput("turtle", "y pos:",default=None, minval=1, maxval=15))

    set_X(array2D, y, x)
    if(check_win(array2D, size) == 1):
        shutdown = 1
        print_gamefield(array2D,size)
        turtle_check_win(size)

        print('X win')

    else:
        print_gamefield(array2D,size)
        robot(array2D, size, x)
        if(check_win(array2D, size) == 1):
            shutdown = 1
            print_gamefield(array2D,size)
            turtle_check_win(size)
            print('O win')
turtle.done()