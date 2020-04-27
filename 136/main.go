package main

import "fmt"

func main() {
	fmt.Println(singleNumber([]int{5, 1, 2, 1, 2}))
}

func singleNumber(nums []int) int {
	result := 0
	for _, val := range nums {
		result ^= val
	}
	return result
}
