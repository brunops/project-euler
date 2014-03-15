#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1024
#define MATRIX_SIZE 80

int main() {
  int curr_number, row, col, i, j;
  int matrix[MATRIX_SIZE][MATRIX_SIZE];

  char buffer[BUFFER_SIZE], *token;
  FILE *fp;


  if ((fp = fopen("matrix.txt", "r")) == NULL) {
    printf("Failed opening file\n");
  }


  while (fgets(buffer, sizeof(char) * BUFFER_SIZE, fp)) {
    token = strtok(buffer, ",");
    matrix[row][0] = atoi(token);

    col = 0;
    while ((token = strtok(NULL, ","))) {
      matrix[row][col++] = atoi(token);
    }

    row++;
  }
  fclose(fp);


  return 0;
}

