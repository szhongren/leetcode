package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(findDuplicates([]int{4, 3, 2, 7, 8, 2, 3, 1}))
}

func findDuplicates(nums []int) []int {
	result := []int{}
	for _, v := range nums {
		i := int(math.Abs(float64(v)) - 1)
		if nums[i] > 0 {
			nums[i] *= -1
		} else {
			result = append(result, i+1)
		}
	}
	return result
}
