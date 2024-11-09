#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
  string first_name, surname;

  cout << "First Name: ";
  cin >> first_name;
  cout << "Surname: ";
  cin >> surname;

  // lower case first name
  for (int i = 0; i < first_name.length(); i++) {
    first_name[i] = tolower(first_name[i]);
  }
  // lower case surname
  for (int i = 0; i < surname.length(); i++) {
    surname[i] = tolower(surname[i]);
  }

  cout << first_name << " " << surname << "\n";

  return 0;
}
