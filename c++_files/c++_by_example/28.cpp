#include <iomanip>
#include <iostream>
using namespace std;

int main() {
  double num;

  cout << "Number with lots of decimal places: ";
  cin >> num;

  cout << fixed << setprecision(2) << num * 2 << "\n";

  return 0;
}
