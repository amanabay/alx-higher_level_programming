#!/usr/bin/node
// Prints My number: <first argument converted in integer>

if (isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
