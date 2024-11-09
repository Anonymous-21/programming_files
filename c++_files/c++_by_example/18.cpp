#include <iostream>
using namespace std;

int main() {
  int num;

  cout << "Number: ";
  cin >> num;

  if (num >= 10 && num <= 20) {
    cout << "Correct\n";
  } else if (num < 10) {
    cout << "Too low\n";
  } else {
    cout << "Too high\n";
  }

  return 0;
}
