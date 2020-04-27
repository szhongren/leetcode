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
		4,
		&TreeNode{
			2,
			&TreeNode{
				1,
				nil,
				nil,
			},
			&TreeNode{
				3,
				nil,
				nil,
			},
		},
		&TreeNode{
			7,
			nil,
			nil,
		},
	}
	fmt.Println(makeGoTree(insertIntoBST(tr, 5)).Print())
}

func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if val > root.Val {
		if root.Right == nil {
			root.Right = &TreeNode{
				val,
				nil,
				nil,
			}
		} else {
			root.Right = insertIntoBST(root.Right, val)
		}
	} else if val < root.Val {
		if root.Left == nil {
			root.Left = &TreeNode{
				val,
				nil,
				nil,
			}
		} else {
			root.Left = insertIntoBST(root.Left, val)
		}
	}
	return root
}
