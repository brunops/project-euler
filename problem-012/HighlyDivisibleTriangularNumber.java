import java.lang.Math;

class HighlyDivisibleTriangularNumber {
  public static void main(String[] args) {
    int number = 0;
    int i = 1;

    while (nod(number) < 500) {
      number += i;
      i++;
    }

    System.out.println("First triangular number with more than 500 divisors is: " + number);
  }

  static int nod(int number) {
    int nod = 0;
    int square_root = (int) Math.sqrt(number);

    for (int i = 1; i <= square_root; i++) {
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
}
