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

func invertTree2(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	queue := []*TreeNode{root}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		// Swap left and right children
		node.Left, node.Right = node.Right, node.Left

		// Add non-nil children to the queue
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}

	return root
}
