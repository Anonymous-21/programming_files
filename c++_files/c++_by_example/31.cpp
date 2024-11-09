#include <cmath>
#include <iostream>
using namespace std;

int main() {
  int radius;
  int area;

  cout << "Radius of circle: ";
  cin >> radius;

  area = M_PI * pow(radius, 2);

  cout << "Area: " << area << "\n";

  return 0;
}
