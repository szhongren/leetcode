package main

import (
	"fmt"
)

func main() {
	matrix := [][]int{
		[]int{1, 2, 3, 4},
		[]int{5, 1, 2, 3},
		[]int{9, 5, 1, 2},
	}
	fmt.Println(isToeplitzMatrix(matrix))
}

func isToeplitzMatrix(matrix [][]int) bool {
	for i := 1; i < len(matrix); i++ {
		l := len(matrix[i])
		currRow := matrix[i]
		prevRow := matrix[i-1]
		for j := 1; j < l; j++ {
			if currRow[j] != prevRow[j-1] {
				return false
			}
		}
	}
	return true
}
