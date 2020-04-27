package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(arrayPairSum([]int{1, 4, 3, 2}))
}

func arrayPairSum(nums []int) int {
	result := 0
	sort.Ints(nums)
	for i := 0; i < len(nums); i += 2 {
		result += nums[i]
	}
	return result
}
