package main

import "fmt"

func main() {
	list := &ListNode{
		1,
		&ListNode{
			2,
			&ListNode{
				3,
				&ListNode{
					4,
					&ListNode{
						5,
						// &ListNode{
						// 	6,
						nil,
						// },
					},
				},
			},
		},
	}
	fmt.Println(middleNode(list).Val)
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	fast := head
	slow := head
	for fast != nil {
		fast = fast.Next
		if fast != nil {
			fast = fast.Next
			slow = slow.Next
		}
	}
	return slow
}
