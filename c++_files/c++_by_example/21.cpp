#include <iostream>
#include <string>
using namespace std;

int main() {
  string first_name, surname, full_name;

  cout << "First Name: ";
  cin >> first_name;
  cout << "Surname: ";
  cin >> surname;

  full_name = first_name + " " + surname;

  cout << "Full Name: " << full_name << "\n";
  cout << "Length of full name: " << full_name.length() << "\n";

  return 0;
}
