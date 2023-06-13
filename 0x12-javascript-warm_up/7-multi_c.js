#!/usr/bin/node
// Prints x times “C is fun”

const num = process.argv[2];

if (isNaN(Number(num))) {
  console.log('Missing number of occurences');
} else {
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
} 
