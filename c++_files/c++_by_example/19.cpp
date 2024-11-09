#include <iostream>
using namespace std;

int main() {
  int num;

  cout << "Number (1, 2 or 3): ";
  cin >> num;

  if (num == 1) {
    cout << "Thank you\n";
  } else if (num == 2) {
    cout << "Well done\n";
  } else if (num == 3) {
    cout << "Correct\n";
  } else {
    cout << "Error message\n";
  }

  return 0;
}
