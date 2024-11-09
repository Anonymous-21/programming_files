#include <iostream>
using namespace std;

int main() {
  int num;

  cout << "Number between 10 and 20 (inclusive): ";
  cin >> num;

  if (num >= 10 && num <= 20) {
    cout << "Thank you\n";
  } else {
    cout << "Incorrect answer\n";
  }

  return 0;
}
