package main

import "fmt"

func main() {
	matrix := [][]int{
		[]int{1, 2, 3},
		[]int{4, 5, 6},
		[]int{7, 8, 9},
	}
	fmt.Println(transpose(matrix))
}

func transpose(A [][]int) [][]int {
	result := [][]int{}
	for i := 0; i < len(A[0]); i++ {
		newRow := []int{}
		for j := 0; j < len(A); j++ {
			newRow = append(newRow, A[j][i])
		}
		result = append(result, newRow)
	}
	return result
}
