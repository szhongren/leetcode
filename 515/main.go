package main

import "fmt"

func main() {
	tr := &TreeNode{
		1,
		&TreeNode{
			3,
			&TreeNode{5, nil, nil},
			&TreeNode{3, nil, nil},
		},
		&TreeNode{
			2,
			nil,
			&TreeNode{9, nil, nil},
		},
	}
	fmt.Println(largestValues(tr))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) []int {
	queue := []*TreeNode{root}
	result := []int{}
	if root == nil {
		return result
	}
	for len(queue) != 0 {
		newQueue := []*TreeNode{}
		max := queue[0].Val
		for _, node := range queue {
			if node.Val > max {
				max = node.Val
			}
			if node.Left != nil {
				newQueue = append(newQueue, node.Left)
			}
			if node.Right != nil {
				newQueue = append(newQueue, node.Right)
			}
		}
		result = append(result, max)
		queue = newQueue
	}
	return result
}
