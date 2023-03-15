#!/usr/bin/node
class Rectangle {
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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
 
  charPrint (c) {
    if (c === undefined) {
      this.print();
    }
    for (let row = 0; row < this.height; row++) {
      let rec = '';
      for (let col = 0; col < this.width; col++) {
        rec += 'C';
      }
      console.log(rec);
    }
  }
}
