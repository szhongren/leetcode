package main

import (
	"fmt"
	"strconv"

	"github.com/disiqueira/gotree"
)

func main() {
	tr := &TreeNode{
		3,
		&TreeNode{
			0,
			nil,
			&TreeNode{
				2,
				&TreeNode{
					1,
					nil,
					nil,
				},
				nil,
			},
		},
		&TreeNode{
			4,
			nil,
			nil,
		},
	}
	fmt.Println(makeGoTree(trimBST(tr, 1, 3)).Print())
}

// Definition for a binary tree node.
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

func trimBST(root *TreeNode, L int, R int) *TreeNode {
	if root == nil {
		return root
	}
	if root.Val >= L && root.Val <= R {
		root.Left = trimBST(root.Left, L, R)
		root.Right = trimBST(root.Right, L, R)
		return root
	}
	if root.Val < L {
		return trimBST(root.Right, L, R)
	}
	if root.Val > R {
		return trimBST(root.Left, L, R)
	}
	return root
}
