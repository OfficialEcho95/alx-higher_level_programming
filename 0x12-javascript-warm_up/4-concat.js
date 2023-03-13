#!/usr/bin/node
if (process.argv[2]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
	if (process.argv.length < 3) {
		console.log('undefined is undefined');
	}
}
