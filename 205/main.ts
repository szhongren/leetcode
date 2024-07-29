function isIsomorphic(s: string, t: string): boolean {
  let forwardMapping = new Map();
  let backwardMapping = new Map();
  for (let i = 0; i < s.length; i++) {
    console.log(forwardMapping);
    console.log(backwardMapping);
    let sourceChar = s[i];
    let targetChar = t[i];
    if (
      forwardMapping.has(sourceChar) &&
      forwardMapping.get(sourceChar) !== targetChar
    )
      return false;
    if (
      backwardMapping.has(targetChar) &&
      backwardMapping.get(targetChar) !== sourceChar
    )
      return false;
    forwardMapping.set(sourceChar, targetChar);
    backwardMapping.set(targetChar, sourceChar);
  }
  return true;
}

console.log(isIsomorphic("egg", "add"));
console.log(isIsomorphic("badc", "baba"));
