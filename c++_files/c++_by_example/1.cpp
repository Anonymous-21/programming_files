#include <iostream>
#include <string>

int main()
{
  std::string first_name;    

  std::cout << "First Name: ";
  std::cin >> first_name;

  std::cout << "Hello " << first_name << "\n";

  return 0;
}
