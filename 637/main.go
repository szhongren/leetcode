package main

import "fmt"

func main() {
	tr := &TreeNode{
		3,
		&TreeNode{9, nil, nil},
		&TreeNode{20,
			&TreeNode{15, nil, nil},
			&TreeNode{7, nil, nil},
		},
	}
	fmt.Println(averageOfLevels(tr))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	queue := []*TreeNode{root}
	result := []float64{}
	if root == nil {
		return result
	}
	for len(queue) != 0 {
		newQueue := []*TreeNode{}
		var sum float64
		for _, node := range queue {
			sum += float64(node.Val)
			if node.Left != nil {
				newQueue = append(newQueue, node.Left)
			}
			if node.Right != nil {
				newQueue = append(newQueue, node.Right)
			}
		}
		result = append(result, sum/float64(len(queue)))
		queue = newQueue
	}
	return result
}
