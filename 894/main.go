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
	for _, v := range allPossibleFBT(7) {
		fmt.Println(makeGoTree(v).Print())
	}
}

func allPossibleFBT(N int) []*TreeNode {
	if N%2 == 0 {
		return []*TreeNode{}
	} else if N == 1 {
		return []*TreeNode{
			&TreeNode{
				0,
				nil,
				nil,
			},
		}
	} else {
		key := map[int][]*TreeNode{
			1: []*TreeNode{
				&TreeNode{
					0,
					nil,
					nil,
				},
			},
		}
		for totalSize := 3; totalSize <= N; totalSize += 2 {
			key[totalSize] = []*TreeNode{}
			for leftSize := 1; leftSize <= totalSize-2; leftSize += 2 {
				for _, newLeftTree := range key[leftSize] {
					for _, newRightTree := range key[totalSize-leftSize-1] {
						newTree := &TreeNode{
							0,
							nil,
							nil,
						}
						newTree.Left = copyTree(newLeftTree) // performance hit, not actually needed
						newTree.Right = copyTree(newRightTree)
						key[totalSize] = append(key[totalSize], newTree)
					}
				}
			}
		}
		return key[N]
	}
}

func copyTree(root *TreeNode) *TreeNode {
	newTree := &TreeNode{
		root.Val,
		nil,
		nil,
	}
	if root.Right != nil {
		newTree.Right = copyTree(root.Right)
	}
	if root.Left != nil {
		newTree.Left = copyTree(root.Left)
	}
	return newTree
}
