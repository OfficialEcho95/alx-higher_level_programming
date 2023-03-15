#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { 
	    // check if the current element matches the search element
      count++; 
	    // increment the count if a match is found
    }
  }
  return count; // return the final count after checking all elements
};
