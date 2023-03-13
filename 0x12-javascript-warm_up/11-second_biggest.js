#!/usr/bin/node
let a = process.argv.slice(2).map(arg => parseInt(arg));

if (process.argv.length  < 3 || process.argv.length < 4) {
	console.log(0);
} else {
	console.log(Math.max(...a));
	// console.log(Math.max(...a)) can be rewritten as
	// console.log(Math.max.apply(null, args));

}
