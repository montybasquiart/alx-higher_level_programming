#!/usr/bin/node
/* A script that prints x times 'C is fun'
*/

const elements = 'C is fun';
const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < x; index++) {
    console.log(elements);
  }
}
