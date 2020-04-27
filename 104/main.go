package main

import (
	"fmt"
	"math"
)

func main() {
	tr := &TreeNode{
		3,
		&TreeNode{9, nil, nil},
		&TreeNode{
			20,
			&TreeNode{15, nil, nil},
			&TreeNode{7, nil, nil},
		},
	}
	fmt.Println(maxDepth(tr))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	} else {
		return int(math.Max(float64(maxDepth(root.Left)+1), float64(maxDepth(root.Right)+1)))
	}
}
