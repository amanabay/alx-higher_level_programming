#!/usr/bin/node

/* function that prints the number of arguments already
  printed and the new argument value */

let numArgs = 0;

exports.logMe = function (item) {
  console.log(numArgs + ': ' + item);
  numArgs++;
};
