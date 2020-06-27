#include <iostream>
#include <vector>

#include "gameBasic.h"

using namespace std;

int main() {
    Gameboard gameboard(17);
    while (!gameboard.finish) {
        gameboard.printBoard();
        int x, y;
        if (gameboard.playerNow == Player1){
            cout << "Player1 turn" << endl;
            do {
                cin >> x >> y;
            } while (gameboard.SetX(x, y) == false);
        }
        else{
            cout << "Player2 turn" << endl;
            do {
                cin >> x >> y;
            } while (gameboard.SetO(x, y) == false);
        }
        gameboard.taketurn();
        if (gameboard.checkWin())
            gameboard.finish = true;
    }
    gameboard.printBoard();
    return 0;
}