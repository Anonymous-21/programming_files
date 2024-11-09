#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
  int num;

  cout << "Integer over 500: ";
  cin >> num;

  num = sqrt(num);

  cout << fixed << setprecision(2) << num << "\n";

  return 0;
}
