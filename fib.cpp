#include <iostream>

int fibonacci(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

int main() {
  for (int p = 0; p < 10; p++) {
    std::cout << fibonacci(p) << " ";
  }
  std::cout << std::endl;
  return 0;
}