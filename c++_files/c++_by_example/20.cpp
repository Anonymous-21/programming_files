#include <iostream>
#include <string>
using namespace std;

int main() {
  string first_name;

  cout << "First Name: ";
  cin >> first_name;

  cout << "Length of name: " << first_name.length() << "\n";

  return 0;
}
