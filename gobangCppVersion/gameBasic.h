#include <iostream>
#include <vector>
using namespace std;
enum Player { Player1,
              Player2 };


class Gameboard {
   private:
    vector<vector<char> > Board;
    int size;
   public:
    bool finish;
    Player playerNow;
    Gameboard(int s);
    void printBoard();
    bool checkWin();
    bool SetX(int xPos, int yPos);
    bool SetO(int xPos, int yPos);
    void taketurn();
};