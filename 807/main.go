package main

import (
	"fmt"
)

func main() {
	fmt.Println(maxIncreaseKeepingSkyline(
		[][]int{
			{3, 0, 8, 4},
			{2, 4, 5, 7},
			{9, 2, 6, 3},
			{0, 3, 1, 0},
		}))
}

func makeArrayWithSameSizeAllZeroes(l int) []int {
	allZeroes := []int{}
	for x := 0; x < l; x++ {
		allZeroes = append(allZeroes, 0)
	}
	return allZeroes
}

func maxIncreaseKeepingSkyline(grid [][]int) int {
	rowMax := makeArrayWithSameSizeAllZeroes(len(grid))
	colMax := makeArrayWithSameSizeAllZeroes(len(grid[0]))
	for i, row := range grid {
		for j, val := range row {
			if val > rowMax[i] {
				rowMax[i] = val
			}
			if val > colMax[j] {
				colMax[j] = val
			}
		}
	}
	result := 0
	for i, row := range grid {
		for j, val := range row {
			min := rowMax[i]
			if colMax[j] < min {
				min = colMax[j]
			}
			result += min - val
		}
	}
	return result
}
