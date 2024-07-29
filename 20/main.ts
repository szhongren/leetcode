function isValid(s: string): boolean {
  let stack: string[] = [];
  for (let char of s) {
    console.log(stack);
    console.log(char);
    if (char === "(" || char === "[" || char === "{") stack.push(char);
    else if (char === ")" && stack[stack.length - 1] !== "(") return false;
    else if (char === "]" && stack[stack.length - 1] !== "[") return false;
    else if (char === "}" && stack[stack.length - 1] !== "{") return false;
    else stack.pop();
  }
  return stack.length === 0;
}

console.log(isValid("()"));
console.log(isValid("()[]{}"));
console.log(isValid("(}"));
console.log(isValid("({)}"));
