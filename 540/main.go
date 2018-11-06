package main

import "fmt"

func main() {
	fmt.Println(singleNonDuplicate([]int{1, 1, 2, 2, 4, 4, 5, 5, 9}))
}

func singleNonDuplicate(nums []int) int {
	return singleNonDuplicateRecur(nums, 0, len(nums))
}

func singleNonDuplicateRecur(nums []int, start int, end int) int {
	if end-1 == start {
		return nums[start]
	} else if end-3 == start {
		if nums[start] != nums[start+1] {
			return nums[start]
		}
		return nums[start+2]
	}
	var result int
	pivot := (end + start) / 2
	curr := nums[pivot]
	if (end-pivot)%2 == 0 {
		// even number on the right
		if nums[pivot-1] != curr {
			// element on the left
			result = singleNonDuplicateRecur(nums, start, pivot)
		} else {
			// element on the right
			result = singleNonDuplicateRecur(nums, pivot-1, end)
		}
	} else {
		// even number on the left
		if nums[pivot-1] != curr {
			// element on the right
			result = singleNonDuplicateRecur(nums, pivot, end)
		} else {
			// element on the left
			result = singleNonDuplicateRecur(nums, start, pivot+1)
		}
	}
	return result
}
