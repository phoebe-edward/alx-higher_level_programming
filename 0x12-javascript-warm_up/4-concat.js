#!/usr/bin/node
let myVar1;
let myVar2;
if (process.argv[2] == null) {
  myVar1 = 'undefined';
  myVar2 = 'undefined';
} else if (process.argv[3] == null) {
  myVar2 = 'undefined';
  myVar1 = process.argv[2];
} else {
  myVar1 = process.argv[2];
  myVar2 = process.argv[3];
}
console.log(myVar1 + ' is ' + myVar2);