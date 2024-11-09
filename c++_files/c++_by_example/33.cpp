#include <iostream>
using namespace std;

int main() {
  int num1, num2;

  cout << "Number: ";
  cin >> num1;
  cout << "Number: ";
  cin >> num2;

  cout << num1 << " divided by " << num2 << " is " << num1 / num2 << " with "
       << num1 % num2 << " remaining\n";

  return 0;
}
