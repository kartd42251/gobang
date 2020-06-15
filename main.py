from myturtle import *
from game_basic import *



def main():
    turtle_init()
    turtle_gamefield()
    shutdown = 0
    size = 15
    user = 1 # 1 for x -1 for y
    array2D = [["." for _ in range(size)] for _ in range(size)]

    while shutdown == 0:
        stupid = 0

        x = int(turtle.numinput("turtle", "x pos:",
                                default=None, minval=1, maxval=size))
        y = int(turtle.numinput("turtle", "y pos:",
                                    default=None, minval=1, maxval=size))
        if(user == 1):

            set_X(array2D, y, x)
        elif(user == -1):
            set_O(array2D, y, x)


        print_gamefield(array2D, size, user)

        if(check_win(array2D, size) == 1):
            shutdown = 1
            print_gamefield(array2D, size, user)
            if(user == 1):
                turtle_check_win(size,"USER1")
            elif(user == -1):
                turtle_check_win(size,"USER2")

        user *= -1


        # else:
        #     print_gamefield(array2D, size)
        #     myrobot_pro(array2D, size)
        #     if(check_win(array2D, size) == 1):
        #         shutdown = 1
        #         print_gamefield(array2D, size)
        #         turtle_check_win(size,"COMP")
        #         print('O win')

    turtle.done()
    
if __name__ == "__main__":
    main()
    
