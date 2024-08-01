function simplifyPath(path: string): string {
  let sections = generateSections(path);
  let stack: string[] = [];
  for (let section of sections) {
    if (section === "..") {
      stack.pop();
    } else if (section === ".") {
      continue;
    } else {
      stack.push(section);
    }
  }
  return "/" + stack.join("/");
}

function generateSections(path: string): string[] {
  let i = 0;
  let results: string[] = [];
  while (true) {
    while (path[i] === "/") i++;
    if (i >= path.length) break;
    let end = path.indexOf("/", i);
    if (end === -1) {
      results.push(path.slice(i));
      break;
    }
    results.push(path.slice(i, end));
    i = end;
  }
  return results;
}

// split by /\/+/
// iterate through words
// if ..
// pop stack
// if .
// continue
// otherwise
// push
// return  stack.join("/")

console.log(simplifyPath("/home/user/Documents/../Pictures"));
