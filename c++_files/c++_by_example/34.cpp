#include <cmath>
#include <iostream>
using namespace std;

int main() {
  int num, side, area, base, height;

  cout << "1) Square\n";
  cout << "2) Triangle\n";
  cout << "\n";
  cout << "Enter a number: ";
  cin >> num;

  if (num == 1) {
    cout << "Side length: ";
    cin >> side;

    area = pow(side, 2);

    cout << "Area: " << area << "\n";
  } else if (num == 2) {
    cout << "Base: ";
    cin >> base;
    cout << "Height: ";
    cin >> height;

    area = (base * height) / 2;

    cout << "Area: " << area << "\n";
  } else {
    cout << "Error\n";
  }

  return 0;
}
