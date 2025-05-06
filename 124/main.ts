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

function maxPathSum(root: TreeNode | null): number {
  if (root === null) return 0;
  let maxes = [maxSumToNode(root.left) + maxSumToNode(root.right) + root.val];

  if (root.left !== null) maxes.push(maxPathSum(root.left));
  if (root.right !== null) maxes.push(maxPathSum(root.right));
  return Math.max(...maxes);
}

function maxSumToNode(root: TreeNode | null): number {
  if (root === null) return 0;
  return root.val + Math.max(maxSumToNode(root.left), maxSumToNode(root.right));
}

// at each node, calculate 3 values
// max with current node (max sum to current from left + current + max sum to current from right)
// max in left tree
// max in right tree
