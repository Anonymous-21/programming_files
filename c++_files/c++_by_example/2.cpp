#include <iostream>
#include <string>
using namespace std;

int main() {
  string first_name, surname;

  cout << "First Name: ";
  cin >> first_name;
  cout << "Surname: ";
  cin >> surname;

  cout << "Hello " << first_name << " " << surname << "\n";

  return 0;
}
