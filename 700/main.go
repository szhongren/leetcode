package main

import (
	"fmt"
	"strconv"

	"github.com/disiqueira/gotree"
)

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
	tree := &TreeNode{
		4,
		&TreeNode{
			2,
			&TreeNode{1, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{7, nil, nil},
	}
	fmt.Println(makeGoTree(searchBST(tree, 2)).Print())
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	res := root
	if root == nil || val == root.Val {
		return res
	} else if val < root.Val {
		res = searchBST(root.Left, val)
	} else if val > root.Val {
		res = searchBST(root.Right, val)
	}
	return res
}
