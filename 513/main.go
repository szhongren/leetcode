package main

import "fmt"

func main() {
	tr := &TreeNode{
		1,
		&TreeNode{
			2,
			&TreeNode{4, nil, nil},
			nil,
		},
		&TreeNode{
			3,
			&TreeNode{
				5,
				&TreeNode{7, nil, nil},
				nil,
			},
			&TreeNode{6, nil, nil},
		},
	}
	fmt.Println(findBottomLeftValue(tr))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findBottomLeftValue(root *TreeNode) int {
	queue := []*TreeNode{root}
	last := 0
	for len(queue) != 0 {
		last = queue[0].Val
		newQueue := []*TreeNode{}
		for _, node := range queue {
			if node.Left != nil {
				newQueue = append(newQueue, node.Left)
			}
			if node.Right != nil {
				newQueue = append(newQueue, node.Right)
			}
		}
		queue = newQueue
	}
	return last
}
