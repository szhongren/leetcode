package main

import "fmt"

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}

func twoSum(nums []int, target int) []int {
	found := make(map[int]int)
	var results = []int{}
	for index, num := range nums {
		if val, ok := found[target-num]; ok {
			results = append(results, val, index)
		} else {
			found[num] = index
		}
	}
	return results
}
