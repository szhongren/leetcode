package main

import (
	"fmt"
	"strconv"

	"github.com/disiqueira/gotree"
)

// It’s possible to build a Cartesian tree from a sequence of data in linear time. Beginning with the empty tree,

// Scan the given sequence from left to right adding new nodes as follows:

// Position the node as the right child of the rightmost node.
// Scan upward from the node’s parent up to the root of the tree until a node is found whose value is greater than the current value.
// If such a node is found, set its right child to be the new node, and set the new node’s left child to be the previous right child.
// If no such node is found, set the new child to be the root, and set the new node’s left child to be the previous tree.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	fmt.Println(makeGoTree(constructMaximumBinaryTree([]int{3, 2, 1, 6, 0, 5})).Print())
	// fmt.Println(makeGoTree(constructMaximumBinaryTree([]int{5, 10, 40, 30, 28})).Print())
}

func makeGoTree(tr *TreeNode) gotree.Tree {
	if tr == nil {
		return nil
	}
	tree := gotree.New(strconv.Itoa(tr.Val))
	if tr.Left != nil {
		tree.AddTree(makeGoTree(tr.Left))
	}
	if tr.Right != nil {
		tree.AddTree(makeGoTree(tr.Right))
	}
	return tree
}

func constructMaximumBinaryTree(nums []int) *TreeNode {
	l := len(nums)
	if l == 0 {
		return nil
	}

	// init
	parents, leftchilds, rightchilds := make([]int, l, l), make([]int, l, l), make([]int, l, l)
	for i := 0; i < l; i++ {
		parents[i] = -1
		leftchilds[i] = -1
		rightchilds[i] = -1
	}
	// assume root is first value
	root := 0
	var last int
	// for each index
	for i := 1; i < l; i++ {
		last = i - 1
		// 2
		//  \
		//   nil
		rightchilds[i] = -1

		for nums[last] <= nums[i] && last != root {
			// go up the tree while current is smaller than nums[last]
			// and not at root
			last = parents[last]
		}
		if nums[last] <= nums[i] {
			// below the point to insert curr
			parents[root] = i
			// root's parent is curr
			leftchilds[i] = root
			// root is left child of curr
			root = i
			// curr is new root
		} else if rightchilds[last] == -1 {
			// last has no right child
			rightchilds[last] = i
			// curr is right child of root
			parents[i] = last
			// curr's parent is last
			leftchilds[i] = -1
			// curr's left child is nil
		} else {
			// last has right child
			parents[rightchilds[last]] = i
			// last's right child's new parent is curr
			leftchilds[i] = rightchilds[last]
			// curr's left child is last's right child
			rightchilds[last] = i
			// last's right child is curr
			parents[i] = last
			// curr's parent is last
		}
	}
	parents[root] = -1
	return constructMaximumBinaryTreeHelper(root, nums, parents, leftchilds, rightchilds)
}

func constructMaximumBinaryTreeHelper(root int, nums []int, parents []int, leftchilds []int, rightchilds []int) *TreeNode {
	if root == -1 {
		return nil
	}
	tr := &TreeNode{0, nil, nil}
	tr.Val = nums[root]
	tr.Left = constructMaximumBinaryTreeHelper(leftchilds[root], nums, parents, leftchilds, rightchilds)
	tr.Right = constructMaximumBinaryTreeHelper(rightchilds[root], nums, parents, leftchilds, rightchilds)
	return tr
}
