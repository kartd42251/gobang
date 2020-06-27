#include "gameBasic.h"

Gameboard::Gameboard(int s) : size(s), finish(false), playerNow(Player1){
    for (int i = 0; i < size; i++) {
        vector<char> BoardRow;
        for (int j = 0; j < size; j++)
            BoardRow.push_back('.');
        Board.push_back(BoardRow);
    }
    for (int i = 0; i < size; i++) {
        Board[0][i] = 'W';
        Board[size - 1][i] = 'W';
        Board[i][size - 1] = 'W';
        Board[i][0] = 'W';
    }
}
void Gameboard::printBoard() {
    cout << "Board::" << endl;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (j == 0 || j == size - 1)
                cout << i % 10 << " ";
            else if (i == 0 || i == size - 1)
                cout << j % 10 << " ";
            else
                cout << Board[i][j] << " ";
        }
        cout << endl;
    }
}

bool Gameboard::SetX(int xPos, int yPos) {
    if (Board[xPos][yPos] != '.')
        return false;
    else
        Board[xPos][yPos] = 'X';
    return true;
}
bool Gameboard::SetO(int xPos, int yPos) {
    if (Board[xPos][yPos] != '.')
        return false;
    else
        Board[xPos][yPos] = 'O';
    return true;
}
void Gameboard::taketurn(){
    if(playerNow == Player1)
        playerNow = Player2;
    else 
        playerNow = Player1;
}

bool Gameboard::checkWin() {
    for (int i = 1; i < size - 1; i++)
        for (int j = 1; j < size - 1; j++) {
            if (Board[i][j] == Board[i][j + 1] &&
                Board[i][j + 1] == Board[i][j + 2] &&
                Board[i][j + 2] == Board[i][j + 3] &&
                Board[i][j + 3] == Board[i][j + 4] &&
                (Board[i][j] == 'X' ||
                 Board[i][j] == 'O') &&
                j + 4 <= size - 2)
                return true;
            if (Board[i][j] == Board[i + 1][j] &&
                Board[i + 1][j] == Board[i + 2][j] &&
                Board[i + 2][j] == Board[i + 3][j] &&
                Board[i + 3][j] == Board[i + 4][j] &&
                (Board[i][j] == 'X' ||
                 Board[i][j] == 'O') &&
                i + 4 <= size - 2)
                return true;
            if (Board[i][j] == Board[i + 1][j + 1] &&
                Board[i + 1][j + 1] == Board[i + 2][j + 2] &&
                Board[i + 2][j + 2] == Board[i + 3][j + 3] &&
                Board[i + 3][j + 3] == Board[i + 4][j + 4] &&
                (Board[i][j] == 'X' ||
                 Board[i][j] == 'O') &&
                i + 4 <= size - 2)
                return true;
        }
    return false;
}
