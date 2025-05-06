#include <iostream>
using namespace std;

class Game {
 public:
  void print_title() {
    cout << endl;
    cout << "*****************************************" << endl;
    cout << "             DUNGEON DELVE               " << endl;
    cout << "*****************************************" << endl;
    cout << endl;
  }
};

int main(void) {
  Game game;
  game.print_title();
}