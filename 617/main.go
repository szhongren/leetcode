package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func makeTree(values []int) *TreeNode {
	if len(values) == 0 {
		return nil
	}
	var treeNodes = []*TreeNode{}
	for _, v := range values {
		node := TreeNode{}
		nodeptr := &node
		if v == -1 {
			treeNodes = append(treeNodes, nil)
		} else {
			node.Val = v
			treeNodes = append(treeNodes, nodeptr)
		}
	}
	length := len(treeNodes)
	for i := 0; i < length>>1; i++ {
		if treeNodes[i] != nil {
			if i*2+1 < length {
				treeNodes[i].Left = treeNodes[i*2+1]
			}
			if i*2+2 < length {
				treeNodes[i].Right = treeNodes[i*2+2]
			}
		}
	}
	return treeNodes[0]
}

func main() {
	fmt.Println(mergeTrees(makeTree([]int{1, 3, 2, 5}), makeTree([]int{2, 1, 3, -1, 4, -1, 7})))
}

func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	return mergeTreesRecur(t1, t2)
}

func mergeTreesRecur(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil && t2 == nil {
		return nil
	}
	if t1 == nil {
		return &TreeNode{
			t2.Val,
			mergeTreesRecur(nil, t2.Left),
			mergeTreesRecur(nil, t2.Right),
		}
	} else if t2 == nil {
		return &TreeNode{
			t1.Val,
			mergeTreesRecur(t1.Left, nil),
			mergeTreesRecur(t1.Right, nil),
		}
	} else {
		return &TreeNode{
			t1.Val + t2.Val,
			mergeTreesRecur(t1.Left, t2.Left),
			mergeTreesRecur(t1.Right, t2.Right),
		}
	}
}
