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

function sortedArrayToBST(nums: number[]): TreeNode | null {
  if (nums.length === 0) return null;
  let middleIndex =
    nums.length % 2 === 0 ? nums.length / 2 : (nums.length - 1) / 2;
  return new TreeNode(
    nums[middleIndex],
    sortedArrayToBST(nums.slice(0, middleIndex)),
    sortedArrayToBST(nums.slice(middleIndex + 1))
  );
}

// 3
// 1
// 5
// 2
// 7
// 3
// 4
// 1/2
// 6
// 2/3
// get middle, set as root node
// middle = if odd then (x - 1) / 2, else x / 2
// left = recur(left half)
// right = recur(right half)
// return root
