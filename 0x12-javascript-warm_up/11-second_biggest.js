#!/usr/bin/node
// Find the second biggest in list of args

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = args[2];
  let secondMax = args[2];

  for (let i = 0; i < args.length; i++) {
    const num = args[i];

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
