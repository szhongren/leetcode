class Trie {
  terminal: boolean;
  children: Map<string, Trie>;
  constructor() {
    this.children = new Map();
    this.terminal = false;
  }

  insert(word: string): void {
    console.log(`inserting ${word}`);
    if (word.length === 0) {
      this.terminal = true;
      return;
    }
    const firstChar = word[0];
    if (!this.children.has(firstChar)) {
      this.children.set(firstChar, new Trie());
    }
    this.children.get(firstChar)?.insert(word.slice(1));
  }

  search(word: string): boolean {
    if (word.length === 0) return this.terminal;
    const firstChar = word[0];
    if (!this.children.has(firstChar)) return false;
    return this.children.get(firstChar)!.search(word.slice(1));
  }

  startsWith(prefix: string): boolean {
    if (prefix.length === 0) return true;
    const firstChar = prefix[0];
    if (!this.children.has(firstChar)) return false;
    return this.children.get(firstChar)!.startsWith(prefix.slice(1));
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

let trie = new Trie();
trie.insert("apple");
console.log(trie.startsWith("b"));
console.log(trie.startsWith("a"));
console.log(trie.startsWith("ap"));
console.log(trie.startsWith("ac"));
console.log(trie.startsWith("app"));
console.log(trie.startsWith("appb"));
console.log(trie.search("app"));
console.log(trie.search("apple"));
console.log(trie.search("apples"));
trie.insert("app");
console.log(trie.search("app"));
