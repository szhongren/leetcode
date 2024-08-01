/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function rightSideView(root: TreeNode | null): number[] {
  if (root === null) return [];
  let results: number[] = [];
  let currentRow: TreeNode[] = [root];
  while (currentRow.length !== 0) {
    results.push(currentRow[currentRow.length - 1].val);
    let newList: TreeNode[] = [];
    for (let node of currentRow) {
      if (node.left) newList.push(node.left);
      if (node.right) newList.push(node.right);
    }
    currentRow = newList;
  }
  return results;
}

// approach
// list of results
// list of root
// while list is not empty
// results.append(list[list.length - 1])
// let newList = []
// for every node in list
// newList.push(node.left, node.right)
// list = newList
