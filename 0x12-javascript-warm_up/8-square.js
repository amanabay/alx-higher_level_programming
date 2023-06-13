#!/usr/bin/node
// Prints a square

let cell = 'X';
const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg - 1; i++) {
    cell += 'X';
  }
  for (let j = 0; j < arg; j++) {
    console.log(cell);
  }
}
