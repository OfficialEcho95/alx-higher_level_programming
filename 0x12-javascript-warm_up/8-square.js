#!/usr/bin/node
let i = 0;

if (process.argv[2]) {
  if (isNaN(+process.argv[2])) {
    console.log('Missing size');
  } else {
    for (; i < process.argv[2]; i++) {
      let row = '';
      for (let j = 0; j < process.argv[2]; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
