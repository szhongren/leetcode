function maxScoreWords(
  words: string[],
  letters: string[],
  score: number[]
): number {
  let getCharScoreIndex = (ch: string) => ch.charCodeAt(0) - "a".charCodeAt(0);
  let scoreWord = (word: string, letters: Map<string, number>): number => {
    let wordScore = 0;
    for (let char of word) {
      //   console.log(char);
      if (!letters.has(char) || letters.get(char) == 0) return 0;
      wordScore += score[getCharScoreIndex(char)];
      //   console.log(getCharScoreIndex(char));
      letters.set(char, letters.get(char) - 1);
    }
    return wordScore;
  };
  let lettersMap = new Map();
  for (let letter of letters) {
    if (!lettersMap.has(letter)) lettersMap.set(letter, 0);
    lettersMap.set(letter, lettersMap.get(letter) + 1);
  }
  for (let word of words) {
    console.log(scoreWord(word, lettersMap));
  }
  return 0;
}

maxScoreWords(
  ["dog", "cat", "dad", "good"],
  ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
  [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);
