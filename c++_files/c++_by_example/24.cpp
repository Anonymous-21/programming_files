#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
  string word;

  cout << "Word: ";
  cin >> word;

  for (int i = 0; i < word.length(); i++) {
    word[i] = toupper(word[i]);
  }

  cout << word << "\n";

  return 0;
}
