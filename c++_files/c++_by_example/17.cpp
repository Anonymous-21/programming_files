#include <iostream>
using namespace std;

int main() {
  int age;

  cout << "Age: ";
  cin >> age;

  if (age >= 18) {
    cout << "You can vote\n";
  } else if (age == 17) {
    cout << "You can learn to drive\n";
  } else if (age == 16) {
    cout << "You can buy a lottery ticket\n";
  } else {
    cout << "You can go Trick-or-Treating\n";
  }

  return 0;
}
