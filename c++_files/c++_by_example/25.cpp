#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
  string first_name, surname, full_name;

  cout << "First Name: ";
  cin >> first_name;

  if (first_name.length() < 5) {
    cout << "Surname: ";
    cin >> surname;

    full_name = first_name + surname;

    for (int i = 0; i < full_name.length(); i++) {
      full_name[i] = toupper(full_name[i]);
    }

    cout << full_name << "\n";
  } else {
    for (int j = 0; j < first_name.length(); j++) {
      first_name[j] = tolower(first_name[j]);
    }

    cout << first_name << "\n";
  }

  return 0;
}
