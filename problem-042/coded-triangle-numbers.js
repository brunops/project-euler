// Coded triangle numbers
// Problem 42
// The nth term of the sequence of triangle numbers is given by, tn = 1/2 * n(n+1); so the first ten triangle numbers are:
//
// 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
//
// By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
//
// Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

/* global require, console */
(function () {
  'use strict';

  var fs = require('fs');

  var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  var triangleNumbers = [1],
      lastIndex = 0;

  function triangleNumber(position) {
    return position * (position + 1) * 0.5;
  }

  function calculateTriangleNumbers(until) {
    while (triangleNumbers[lastIndex] < until) {
      lastIndex++;

      // lastIndex is an array index, the triangleNumber position value
      // starts with 1, that's why + 1
      triangleNumbers[lastIndex] = triangleNumber(lastIndex + 1);
    }
  }

  function wordNumber(word) {
    return word.split('').reduce(function (prev, curr) {
      return prev + letterNumber(curr);
    }, 0);
  }

  // Letter index starting with 1
  function letterNumber(letter) {
    return alphabet.indexOf(letter) + 1;
  }

  fs.readFile('words.txt', 'utf8', function (e, data) {
    var words = data.split(','),
        currWordNumber = 0,
        totalTriangleWords = 0,
        i = 0;

    for (; i < words.length; ++i) {
      currWordNumber = wordNumber(words[i].replace(/"/g, ''));

      if (triangleNumbers[lastIndex] < currWordNumber) {
        calculateTriangleNumbers(currWordNumber);
      }

      if (triangleNumbers.indexOf(currWordNumber) > -1) {
        totalTriangleWords += 1;
      }
    }

    console.log(totalTriangleWords);
  });
}());
