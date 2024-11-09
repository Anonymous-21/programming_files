#include <iostream>
using namespace std;

int main() {
  float total_bill;
  int diners;

  cout << "Total bill: ";
  cin >> total_bill;
  cout << "Number of diners: ";
  cin >> diners;

  cout << "Each person must pay: " << total_bill / diners << "\n";

  return 0;
}
