#!/usr/bin/node
// Imports an array and computes a new array.

const list = require('./100-data.js').list;

const newList = list.map((value, index) => {
  return value * index;
});

console.log(list);
console.log(newList);
