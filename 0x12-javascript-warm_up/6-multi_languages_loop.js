#!/usr/bin/node
let i = 0;
let message = '';

while (i < 3) {
  switch (i) {
    case 0:
      message += 'C is fun\n';
      break;
    case 1:
      message += 'Python is cool\n';
      break;
    case 2:
      message += 'JavaScript is amazing';
      break;
  }
  i++;
}

console.log(message);
