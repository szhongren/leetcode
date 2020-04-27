package main

import "fmt"

func main() {
	fmt.Println(dailyTemperatures([]int{73, 74, 75, 71, 69, 72, 76, 73}))
}

func dailyTemperatures(T []int) []int {
	result := []int{}
	for i, temp1 := range T {
		for j := i + 1; j < len(T); j++ {
			temp2 := T[j]
			if temp2 > temp1 {
				result = append(result, j-i)
				break
			}
			if j == len(T)-1 {
				result = append(result, 0)
			}
		}
	}
	result = append(result, 0)
	return result
}
