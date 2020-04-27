package main

import "fmt"

func main() {
	matrix := [][]int{
		[]int{1, 2},
		[]int{3, 4},
	}
	fmt.Println(matrixReshape(matrix, 1, 4))
}

func matrixReshape(nums [][]int, r int, c int) [][]int {
	if len(nums) == 0 || len(nums)*len(nums[0]) != r*c {
		return nums
	}
	result := [][]int{}
	for i := 0; i < r; i++ {
		newRow := make([]int, c)
		result = append(result, newRow)
	}
	newI := 0
	newJ := 0
	for _, row := range nums {
		for _, cell := range row {
			result[newI][newJ] = cell
			newJ++
			if newJ == c {
				newI++
				newJ = 0
			}
		}
	}
	return result
}
