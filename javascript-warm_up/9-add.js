#!/usr/bin/node
// Add function that return the sum of two number

function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
