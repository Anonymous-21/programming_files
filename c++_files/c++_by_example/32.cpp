#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
  float radius, depth, area, volume;

  cout << "Radius: ";
  cin >> radius;
  cout << "Depth: ";
  cin >> depth;

  area = M_PI * pow(radius, 2);
  volume = area * depth;

  cout << "Volume: " << fixed << setprecision(3) << volume << "\n";

  return 0;
}
