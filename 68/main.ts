function fullJustify(words: string[], maxWidth: number): string[] {
  if (words.length === 0) return [];
  let start = 0;
  let end = 1;
  let result: string[] = [];
  while (true) {
    let total_length = words[start].length;
    while (end < words.length && total_length < maxWidth) {
      total_length += 1 + words[end++].length;
    }
    if (total_length > maxWidth) {
      end--;
    }
    if (end == words.length) {
      break;
    }
    result.push(getJustifiedLine(words.slice(start, end), maxWidth));
    start = end;
    end = start + 1;
  }
  let lastLine = words.slice(start).join(" ");
  lastLine += " ".repeat(maxWidth - lastLine.length);
  result.push(lastLine);
  return result;
}

function getJustifiedLine(words: string[], maxWidth: number): string {
  let totalSpaces =
    maxWidth - words.map((x) => x.length).reduce((a, b) => a + b, 0);
  let numberOfSpaces = words.length - 1;
  let baseSpaces =
    numberOfSpaces > 0 ? Math.floor(totalSpaces / numberOfSpaces) : totalSpaces;
  let extraPaddedSpaces = totalSpaces % numberOfSpaces;
  let result = "";
  for (let i = 0; i < words.length; i++) {
    result += words[i];
    if (i === words.length - 1 && i !== 0) break;
    result += " ".repeat(baseSpaces);
    if (i < extraPaddedSpaces) {
      result += " ";
    }
  }
  return result;
}

// pseudocode
// get accumulator and index
// for word in list at index
// add length + 1 to accumulator
// if accumulator == maxWidth, this should be a new line
// if accumulator > maxWidth, this minus the current word should be a new line

for (var line of fullJustify(
  ["This", "is", "an", "example", "of", "text", "justification."],
  16
))
  console.log(line);

for (var line of fullJustify(
  ["What", "must", "be", "acknowledgment", "shall", "be"],
  16
))
  console.log(line);

for (var line of fullJustify(
  [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
  ],
  20
))
  console.log(line);
