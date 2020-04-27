package main

import (
	"fmt"
	"strconv"

	"github.com/disiqueira/gotree"
)

func main() {
	tr := &TreeNode{
		5,
		&TreeNode{
			3,
			&TreeNode{
				2,
				&TreeNode{1, nil, nil},
				nil,
			},
			&TreeNode{4, nil, nil},
		},
		&TreeNode{
			6,
			nil,
			&TreeNode{
				8,
				&TreeNode{7, nil, nil},
				&TreeNode{9, nil, nil},
			},
		},
	}
	fmt.Println(makeGoTree(increasingBST(tr)).Print())
}

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

func increasingBST(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	for root.Left != nil {
		parent := root.Left
		root.Left = parent.Right
		parent.Right = root
		root = parent
	}
	root.Right = increasingBST(root.Right)
	return root
}
