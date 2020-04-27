package main

import "fmt"

func main() {
	fmt.Println(distributeCandies([]int{1, 1, 2, 2, 3, 3}))
}

func distributeCandies(candies []int) int {
	count := map[int]int{}
	for _, v := range candies {
		if _, ok := count[v]; !ok {
			count[v] = 1
		} else {
			count[v]++
		}
	}
	total := len(count)
	if total > len(candies)/2 {
		total = len(candies) / 2
	}
	return total
}
