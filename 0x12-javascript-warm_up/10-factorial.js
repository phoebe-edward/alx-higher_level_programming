#!/usr/bin/node
function fact (a) {
  if (a === 1) {
    return (a);
  } else {
    return (a * fact(a - 1));
  }
}
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  const a = parseInt(process.argv[2]);
  console.log(fact(a));
}
