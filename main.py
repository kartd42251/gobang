from myturtle import *
from game_basic import *
from robottest import *

def main():
    turtle_init()
    turtle_gamefield()
    shutdown = 0
    size = 15
    array2D = [["." for _ in range(size)] for _ in range(size)]
    while shutdown == 0:
        print_gamefield(array2D, size)
        x = int(turtle.numinput("turtle", "x pos:",
                                default=None, minval=1, maxval=size))
        y = int(turtle.numinput("turtle", "y pos:",
                                default=None, minval=1, maxval=size))

        set_X(array2D, y, x)
        if(check_win(array2D, size) == 1):
            shutdown = 1
            print_gamefield(array2D, size)
            turtle_check_win(size,"USER")

            print('X win')

        else:
            print_gamefield(array2D, size)
            robot(array2D, size)
            if(check_win(array2D, size) == 1):
                shutdown = 1
                print_gamefield(array2D, size)
                turtle_check_win(size,"COMP")
                print('O win')

    turtle.done()
if __name__ == "__main__":
    main()
    
