package main

import (
	"fmt"
	"strconv"

	"github.com/disiqueira/gotree"
)

func main() {
	tr := &TreeNode{
		4,
		&TreeNode{
			2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{
			7,
			&TreeNode{6, nil, nil},
			&TreeNode{9, nil, nil},
		},
	}
	fmt.Println(makeGoTree(invertTree(tr)).Print())
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

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	temp := invertTree(root.Left)
	root.Left = invertTree(root.Right)
	root.Right = temp
	return root
}
