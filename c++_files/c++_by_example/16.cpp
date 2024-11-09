#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
  string choice1, choice2;

  cout << "Is it raining? ";
  getline(cin, choice1);

  for (int i = 0; i < choice1.length(); i++) {
    choice1[i] = tolower(choice1[i]);
  }

  if (choice1 == "yes") {
    cout << "Is it windy? ";
    getline(cin, choice2);

    for (int j = 0; j < choice2.length(); j++) {
      choice2[j] = tolower(choice2[j]);
    }

    if (choice2 == "yes") {
      cout << "It is too windy for an umbrella\n";
    } else {
      cout << "Take an umbrella\n";
    }
  } else {
    cout << "Enjoy your day\n";
  }

  return 0;
}
