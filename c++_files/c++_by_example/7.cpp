#include <iostream>
#include <string>
using namespace std;

int main() {
  string name;
  int age;

  cout << "Name: ";
  getline(cin, name);
  cout << "Age: ";
  cin >> age;

  cout << name << " next birthday you will be " << age << "\n";

  return 0;
}
