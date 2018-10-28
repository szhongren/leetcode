package main

import (
	"fmt"
	"reflect"
)

func main() {
	tree1 := &TreeNode{
		1,
		nil,
		nil,
	}
	tree2 := &TreeNode{
		1,
		&TreeNode{
			2,
			nil,
			nil,
		},
		nil,
	}
	fmt.Println(leafSimilar(tree1, tree2))
}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	return reflect.DeepEqual(getLeafSeq(root1), getLeafSeq(root2))
}

func getLeafSeq(tree *TreeNode) []int {
	result := []int{}
	if tree == nil {
		return result
	} else if tree.Left == nil && tree.Right == nil {
		result = append(result, tree.Val)
	} else {
		result = append(getLeafSeq(tree.Left), getLeafSeq(tree.Right)...)
	}

	return result
}
