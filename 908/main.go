package main

import "fmt"

func main() {
	fmt.Println(smallestRangeI([]int{1}, 0))
}

func smallestRangeI(A []int, K int) int {
	max := A[0]
	min := A[0]
	for _, val := range A {
		if val < min {
			min = val
		}
		if val > max {
			max = val
		}
	}
	res := max - min - 2*K
	if res < 0 {
		return 0
	} else {
		return res
	}
}
