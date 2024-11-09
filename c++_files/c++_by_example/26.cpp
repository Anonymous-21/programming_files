#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
  string word;

  cout << "Word: ";
  cin >> word;

  if (word[0] == 'a' || word[0] == 'e' || word[0] == 'i' || word[0] == 'o' ||
      word[0] == 'u') {
    word = word + "way";
    for (int i = 0; i < word.length(); i++) {
      word[i] = tolower(word[i]);
    }
  } else {
    word = word.substr(1) + word[0] + "ay";
    for (int j = 0; j < word.length(); j++) {
      word[j] = tolower(word[j]);
    }
  }

  cout << word << "\n";

  return 0;
}
