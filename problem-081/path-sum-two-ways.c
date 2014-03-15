#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1024
#define MATRIX_SIZE 80

#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))

int main() {
  int curr_number, row, col, i, j;
  int matrix[MATRIX_SIZE][MATRIX_SIZE];

  char buffer[BUFFER_SIZE], *token;
  FILE *fp;


  if ((fp = fopen("matrix.txt", "r")) == NULL) {
    printf("Failed opening file\n");
  }


  row = 0;
  while (fgets(buffer, sizeof(char) * BUFFER_SIZE, fp)) {
    token = strtok(buffer, ",");
    matrix[row][0] = atoi(token);

    col = 1;
    while ((token = strtok(NULL, ","))) {
      matrix[row][col++] = atoi(token);
    }

    row++;
  }
  fclose(fp);

  // Calculate paths for last row and last column
  for (i = MATRIX_SIZE - 2; i >= 0; i--) {
    matrix[MATRIX_SIZE - 1][i] += matrix[MATRIX_SIZE - 1][i + 1];
    matrix[i][MATRIX_SIZE - 1] += matrix[i + 1][MATRIX_SIZE - 1];
  }



  for (i = MATRIX_SIZE - 2; i >= 0; i--) {
    for (j = MATRIX_SIZE - 2; j >= 0; j--) {
      matrix[i][j] += MIN(matrix[i + 1][j], matrix[i][j + 1]);
    }
  }

  printf("Smallest sum path: %d\n", matrix[0][0]);

  return 0;
}

