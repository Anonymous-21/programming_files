#include <iostream>
using namespace std;

int main() {
  int weight_kgs;

  cout << "Weight in kilograms: ";
  cin >> weight_kgs;

  cout << "Weight in pounds: " << weight_kgs * 2.204 << "\n";

  return 0;
}
