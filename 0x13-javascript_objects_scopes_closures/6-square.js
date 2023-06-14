#!/usr/bin/node
// Define Square class that inherits from Rectangle

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
