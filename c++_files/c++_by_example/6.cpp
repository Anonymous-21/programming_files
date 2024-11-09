#include <iostream>
using namespace std;

int main() {
  int total, eaten;

  cout << "Total pizza slices: ";
  cin >> total;
  cout << "Pizza slices eaten: ";
  cin >> eaten;

  cout << "Pizza slices remaining: " << total - eaten << "\n";

  return 0;
}
