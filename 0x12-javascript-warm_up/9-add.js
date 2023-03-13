#!/usr/bin/node
if (process.argv[2]) {
  if (isNaN(+process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log(add(+process.argv[2], +process.argv[3]));
  }
} else {
  console.log('No argument');
}

function add(a, b) {
	return a + b;
}
