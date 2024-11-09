#include <iostream>
using namespace std;

int main() {
  int num1, num2;

  cout << "Number: ";
  cin >> num1;
  cout << "Number: ";
  cin >> num2;

  if (num1 > num2) {
    cout << num2 << "\n";
    cout << num1 << "\n";
  } else {
    cout << num1 << "\n";
    cout << num2 << "\n";
  }

  return 0;
}
