package main

import "fmt"

func main() {
	fmt.Println(peakIndexInMountainArray([]int{0, 2, 1, 0}))
}

func peakIndexInMountainArray(A []int) int {
	peak := -1
	peakIndex := 0
	for i, v := range A {
		if v > peak {
			peak = v
			peakIndex = i
		} else {
			break
		}
	}
	return peakIndex
}
