#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 1024

int main() {
  char curr;

  char buffer[BUFFER_SIZE];
  FILE *fp;

  if ((fp = fopen("matrix.txt", "r"))) {
    fgets(buffer, sizeof(char) * BUFFER_SIZE, fp);
    printf("%s", buffer);
  }

  fclose(fp);

  return 0;
}

