#include <iostream>
#include <string>
using namespace std;

int main() {
  string rhyme;
  int start_num, end_num;

  cout << "First line of nursery rhyme: ";
  getline(cin, rhyme);

  cout << "Starting Number: ";
  cin >> start_num;
  cout << "Ending Number: ";
  cin >> end_num;

  for (int i = start_num; i < end_num; i++) {
    cout << rhyme[i];
  }
  cout << "\n";

  return 0;
}
