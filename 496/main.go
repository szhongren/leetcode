package main

import "fmt"

func main() {
	fmt.Println(nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2}))
}

func nextGreaterElement(findNums []int, nums []int) []int {
	result := []int{}
	for _, a := range findNums {
		found := false
		nextLarger := -1
		for _, b := range nums {
			if b == a {
				found = true
				continue
			}
			if found && b > a && nextLarger == -1 {
				nextLarger = b
			}
		}
		result = append(result, nextLarger)
	}
	return result
}
