// Digit fifth powers
// Problem 30
// Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

// 1634 = 1^4 + 6^4 + 3^4 + 4^4
// 8208 = 8^4 + 2^4 + 0^4 + 8^4
// 9474 = 9^4 + 4^4 + 7^4 + 4^4
// As 1 = 1^4 is not a sum it is not included.

// The sum of these numbers is 1634 + 8208 + 9474 = 19316.

// Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#include <stdio.h>
#include <math.h>

// 9^5 * 16 => 6 digits
#define UPPER_BOUND 944784

unsigned int sum_of_powered_digits(int number, int power);

int main() {
  int i;
  unsigned int total = 0;

  for (i = 10; i < UPPER_BOUND; ++i) {
    if (i == (int) sum_of_powered_digits(i, 5)) {
      total += i;
    }
  }

  printf("%u\n", total);

  return 0;
}

unsigned int sum_of_powered_digits(int number, int power) {
  unsigned int total = 0;
  int digit;

  while (number > 0) {
    digit = number % 10;
    number /= 10;
    total += (unsigned int) pow(digit, power);
  }

  return total;
}
