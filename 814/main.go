package main

import (
	"fmt"
	"strconv"

	"github.com/disiqueira/gotree"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
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

func main() {

	tr := &TreeNode{
		1,
		nil,
		&TreeNode{
			0,
			&TreeNode{
				0,
				nil,
				nil,
			},
			&TreeNode{
				1,
				nil,
				nil,
			},
		},
	}
	fmt.Println(makeGoTree(pruneTree(tr)).Print())
}

func pruneTree(root *TreeNode) *TreeNode {
	result, _ := pruneTreeRecur(root)
	return result
}

func pruneTreeRecur(root *TreeNode) (*TreeNode, bool) {
	keepRoot := false
	if root.Right != nil {
		rootRight, keep := pruneTreeRecur(root.Right)
		keepRoot = keepRoot || keep
		root.Right = rootRight
	}
	if root.Left != nil {
		rootLeft, keep := pruneTreeRecur(root.Left)
		keepRoot = keepRoot || keep
		root.Left = rootLeft
	}
	if root.Left == nil && root.Right == nil {
		if root.Val == 1 {
			return root, true
		} else {
			return nil, false
		}
	}
	if keepRoot {
		return root, true
	} else {
		return nil, false
	}
}
