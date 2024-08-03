function addBinary(a: string, b: string): string {
  return addBinaryRecur(a, b, false, "");
}

function addBinaryRecur(
  a: string,
  b: string,
  carry: boolean,
  result: string
): string {
  console.log(`"${a}"`);
  console.log(`"${b}"`);
  console.log(carry);
  console.log(result);
  console.log("---------------------------------------");
  if (a.length === 0 && b.length === 0) return (carry ? "1" : "") + result;
  else if (a.length === 0) {
    let charA = "0";
    let charB = b[b.length - 1];
    let [bit, nextCarry] = binaryBitwiseAdd(charA, charB, carry);
    return addBinaryRecur(
      "",
      b.slice(0, b.length - 1),
      nextCarry,
      bit + result
    );
  } else if (b.length === 0) {
    let charA = a[a.length - 1];
    let charB = "0";
    let [bit, nextCarry] = binaryBitwiseAdd(charA, charB, carry);
    return addBinaryRecur(
      a.slice(0, a.length - 1),
      "",
      nextCarry,
      bit + result
    );
  } else {
    let charA = a[a.length - 1];
    let charB = b[b.length - 1];
    let [bit, nextCarry] = binaryBitwiseAdd(charA, charB, carry);
    return addBinaryRecur(
      a.slice(0, a.length - 1),
      b.slice(0, b.length - 1),
      nextCarry,
      bit + result
    );
  }
}

function binaryBitwiseAdd(
  a: string,
  b: string,
  carry: boolean
): [string, boolean] {
  if (a === "0" && b === "0") {
    return [carry ? "1" : "0", false];
  } else if (a === "0" && b === "1") {
    return [carry ? "0" : "1", carry];
  } else if (a === "1" && b === "0") {
    return [carry ? "0" : "1", carry];
  } else if (a === "1" && b === "1") {
    return [carry ? "1" : "0", true];
  }
  return ["", false];
}

// recursive
// pass along the carry
// tail recursion so pass along the total

// 0, 0
// 0, 1
// 1, 0
// 1, 1

//   101
// 11101
//   1
//   t

console.log(addBinary("11", "1"));
console.log(addBinary("1010", "1011"));
