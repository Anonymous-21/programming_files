#include <iostream>
using namespace std;

int main() {
  int num1, num2;

  cout << "Number over 100: ";
  cin >> num1;
  cout << "Number under 10: ";
  cin >> num2;

  cout << num1 << " is " << num1 / num2 << " times " << num2 << "\n";

  return 0;
}
