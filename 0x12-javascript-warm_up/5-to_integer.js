#!/usr/bin/node
/* A script that prints the first argument converted in integer if the first
argument can be converted to an integer
*/

const arg = process.argv[2];
const convertedNumbers = Number(arg);

if (isNaN(convertedNumbers)) {
  console.log('My number:', convertedNumbers);
} else {
  console.log('Not a number');
}
