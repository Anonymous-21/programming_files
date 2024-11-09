#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
  string color;

  cout << "Favourite Color: ";
  cin >> color;

  for (int i = 0; i < color.length(); i++) {
    color[i] = tolower(color[i]);
  }

  if (color == "red") {
    cout << "I like red too\n";
  } else {
    cout << "I don't like " << color << ", I prefer red\n";
  }

  return 0;
}
