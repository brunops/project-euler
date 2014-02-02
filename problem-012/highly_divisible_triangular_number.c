#include <math.h>
#include <stdio.h>

int number_of_divisors(int number);

int main() {
  int triangular_number = 0;
  int inc = 1;

  while (number_of_divisors(triangular_number) < 500) {
    triangular_number += inc;
    inc++;
  }

  printf("First triangular number with at least 500 divisors: %d", triangular_number);

  return 0;
}

int number_of_divisors(int number) {
  int i;
  int nod = 0;
  int square_root = (int) sqrt(number);

  for (i = 1; i <= square_root; i++) {
    if (number % i == 0) {
      nod += 2;
    }
  }

  // adjust for perfect squares
  if (square_root * square_root == number) {
    nod--;
  }

  return nod;
}

