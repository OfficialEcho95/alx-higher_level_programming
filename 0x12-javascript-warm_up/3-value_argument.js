#!/usr/bin/node
const args = process.argv.slice(2);
let numArgs = 0;

for (let arg in args) {
	numArgs++;
}

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs >= 1) {
  console.log(args.join(' '));
}
