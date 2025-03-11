const stack = [];
let number = 10000000;

while ((number / 2) >= 1) {
  stack.push(number % 2);
  number = Math.floor(number / 2);
}
stack.push(1);

result = "";
while ((stack.length) > 0) {
  result += `${stack.pop()}`;
}

console.log(result)







