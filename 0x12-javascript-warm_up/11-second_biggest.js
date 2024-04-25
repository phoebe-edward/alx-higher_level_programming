#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv.length === 3) {
  console.log(0);
} else {
  let a = parseInt(process.argv[2]);
  let i = 2;
  let max = a;
  while (!(isNaN(a))) {
    if (a > max) {
      max = a;
    }
    i++;
    a = parseInt(process.argv[i]);
  }
  a = parseInt(process.argv[2]);
  i = 2;
  let secMax;
  if (a === max) {
    secMax = parseInt(process.argv[3]);
  } else {
    secMax = a;
  }
  while (!(isNaN(a))) {
    if (a > secMax && a !== max) {
      secMax = a;
    }
    i++;
    a = parseInt(process.argv[i]);
  }
  console.log(secMax);
}
