#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let rec = '';
      for (let col = 0; col < this.width; col++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
};
