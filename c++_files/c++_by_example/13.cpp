#include <iostream>
using namespace std;

int main() {
  int num;

  cout << "Number under 20: ";
  cin >> num;

  if (num >= 20) {
    cout << "Too high\n";
  } else {
    cout << "Thank you\n";
  }

  return 0;
}
