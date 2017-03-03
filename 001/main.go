// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:

// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

package main

import "fmt"

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int) // have to use make to have a mutable map
	res := make([]int, 0)
	for i, v := range nums {
		val, found := seen[target - v]
		if found {
			res = append(res, val) // result of append is the new slice
			res = append(res, i)
			break
		} else {
			seen[v] = i // the data is weird, the [n * 2] holds key, the [n * 2 + 1] holds value
		}
	}
	return res
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 5))
}
