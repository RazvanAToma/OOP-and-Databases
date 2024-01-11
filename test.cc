#include <iostream>

int main() {
  // Create an array of car brands
  std::string carBrands[] = {"Toyota", "Honda", "Ford", "Chevrolet", "Nissan"};

  // Print each car brand using a for loop
  for (int i = 0; i < sizeof(carBrands) / sizeof(carBrands[0]); ++i) {
    std::cout << carBrands[i] << std::endl;
  }

  return 0;
}