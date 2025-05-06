class WordDictionary {
  terminal: boolean;
  children: Map<string, WordDictionary>;
  constructor() {
    this.children = new Map();
    this.terminal = false;
  }

  addWord(word: string): void {
    if (word.length === 0) {
      this.terminal = true;
      return;
    }
    const firstChar = word[0];
    if (!this.children.has(firstChar)) {
      this.children.set(firstChar, new WordDictionary());
    }
    this.children.get(firstChar)?.addWord(word.slice(1));
  }

  search(word: string): boolean {
    if (word.length === 0) return this.terminal;
    const firstChar = word[0];
    if (firstChar === ".") {
      return Array.from(this.children.values())
        .map((value) => value.search(word.slice(1)))
        .some((b) => b);
    }
    if (!this.children.has(firstChar)) return false;
    return this.children.get(firstChar)!.search(word.slice(1));
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

let wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
console.log(wordDictionary.search("pad")); // return False
console.log(wordDictionary.search("bad")); // return True
console.log(wordDictionary.search(".ad")); // return True
console.log(wordDictionary.search("b.."));
