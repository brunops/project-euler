// Names scores
// Problem 22
// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

// What is the total of all the name scores in the file?

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILESIZE 50000

int name_score(const char *name, unsigned int position);
int sortstring(void const *str1, void const *str2);

int main() {
  int position = 0, i;

  char **names;
  char buffer[FILESIZE];

  const char separator[2] = ",";

  char *token;

  unsigned long total = 0;

  // allocate memory for 6000 words
  names = malloc(6000 * sizeof(char *));

  while (fgets(buffer, FILESIZE * sizeof(char), stdin)) {
    // remove newline of the end of the file
    buffer[strlen(buffer) - 1] = 0;

    token = strtok(buffer, separator);
    while (token != NULL) {
      // remove last quote by shortening token by one
      token[strlen(token) - 1] = 0;

      // disregard first quote by passing string starting on position 1
      names[position++] = &token[1];

      token = strtok(NULL, separator);
    }
  }

  // SORT SHIT OUT
  qsort(names, position, sizeof(char *), sortstring);

  for (i = 0; i < position; i++) {
    total += name_score(names[i], i + 1);
  }

  printf("%lu", total);

  return 0;
}

int sortstring(void const *str1, void const *str2) {
  return (strcmp(*(char **)str1, *(char **)str2));
}

int name_score(const char *name, unsigned int position) {
  int score = 0, i;

  for (i = 0; name[i] != '\0'; i++) {
    score += name[i] - 'A' + 1;
  }

  return score * position;
}
