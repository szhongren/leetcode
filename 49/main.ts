function groupAnagrams(strs: string[]): string[][] {
  let signatures: Map<string, string[]> = new Map();
  let cache = new Map();
  function getSignature(word: string) {
    if (cache.has(word)) return cache.get(word);
    let signature = word.split("").sort().join("");
    cache.set(word, signature);
    return signature;
  }
  for (let word of strs) {
    let signature = getSignature(word);
    if (!signatures.has(signature)) signatures.set(signature, []);
    signatures.get(signature).push(word);
  }

  let result: string[][] = [];
  for (let value of signatures.values()) result.push(value);
  return result;
}

// for word in words
// get signature (sorted letters)
// put into a list or append for each anagram signature
// at end, append all to list

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
