#include <iostream>
using namespace std;

int main() {
  int days, hours, mins, secs;

  cout << "Days: ";
  cin >> days;

  hours = days * 24;
  mins = hours * 60;
  secs = mins * 60;

  cout << days << " days have " << hours << " hours, " << mins
       << " minutes and " << secs << " seconds\n";

  return 0;
}
