// Names scores
// Problem 22
// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

// What is the total of all the name scores in the file?
/* global console, require */
(function () {
  'use strict';

  var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  function name_score(name, position) {
    var score = 0, i;

    for (i = 0; i < name.length; i++) {
      score += alphabet.indexOf(name[i]) + 1;
    }

    return score * position;
  }

  var fs = require('fs');

  var total_score = 0, position = 0;
  fs.readFile('names.txt', 'utf-8', function(e, names) {
    if (e) return e;

    // remove all quotes
    names = names.replace(/"/g, '');

    names.split(',').sort().forEach(function(name) {
      total_score += name_score(name, ++position);
    });

    console.log(total_score);
  });
}());
