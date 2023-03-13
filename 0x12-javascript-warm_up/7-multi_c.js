#!/usr/bin/node
let i = 0;

if (process.argv[2]) {
  if (isNaN(+process.argv[2])) {
    console.log('Missing number of occurrences');
  } else {
    while (i < process.argv[2]) {
      console.log('C is fun');
      i++;
    }
  }
}
