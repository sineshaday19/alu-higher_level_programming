#!/usr/bin/node
// Convert into integer

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
