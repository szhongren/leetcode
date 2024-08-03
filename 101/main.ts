function isSymmetric(root: TreeNode | null): boolean {
  if (root === null) return true;
  let row = [root];
  let allNulls = false;
  while (!allNulls) {
    console.log(row);
    allNulls = true;
    let start = 0;
    let end = row.length - 1;
    let newRow: (TreeNode | null)[] = [];
    while (start < end) {
      console.log(start, end);
      let front = row[start++];
      let back = row[end--];
      if (front === null && back === null) continue;
      if (front === null || back === null) return false;
      if (front.val !== back.val) return false;
      // if both nulls, continue
      // if 1 null, return false
      // if both not null, check if both values are equal
    }

    for (let i = 0; i < row.length; i++) {
      let node = row[i];
      if (node === null) newRow.push(null, null);
      else {
        allNulls = false;
        newRow.push(node.left, node.right);
      }
    }
    row = newRow;
  }
  return true;
}
