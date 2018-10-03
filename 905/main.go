package main

import (
	"fmt"
)

func main() {
	fmt.Println(sortArrayByParity([]int{3, 1, 2, 4}))
}

func sortArrayByParity(A []int) []int {
	head := 0
	tail := len(A) - 1
	for head <= tail {
		if A[head]%2 == 1 {
			A[head], A[tail] = A[tail], A[head]
			tail--
			head--
		}
		head++
	}
	return A
}
