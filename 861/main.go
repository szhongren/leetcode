package main

import (
	"fmt"
	"math"
)

func main() {
	matrix := [][]int{
		[]int{0, 0, 1, 1},
		[]int{1, 0, 1, 0},
		[]int{1, 1, 0, 0},
	}
	fmt.Println(matrixScore(matrix))
	for _, row := range matrix {
		fmt.Println(row)
	}
}

func matrixScore(A [][]int) int {
	numCols := len(A[0])
	numRows := len(A)
	for i := 0; i < numRows; i++ {
		if A[i][0] == 0 {
			flipRow(A, i)
		}
	}
	for i := 1; i < numCols; i++ {
		count0s, count1s := 0, 0
		for j := 0; j < numRows; j++ {
			if A[j][i] == 0 {
				count0s++
			} else {
				count1s++
			}
		}
		if count0s > count1s {
			flipCol(A, i)
		}
	}
	result := 0.0
	for i := 0; i < numRows; i++ {
		for j := 0; j < numCols; j++ {
			result += math.Pow(2, float64(numCols-j-1)) * float64(A[i][j])
		}
	}
	return int(result)
}

func flipRow(A [][]int, row int) {
	for i := 0; i < len(A[0]); i++ {
		if A[row][i] == 0 {
			A[row][i] = 1
		} else {
			A[row][i] = 0
		}
	}
}

func flipCol(A [][]int, col int) {
	for i := 0; i < len(A); i++ {
		if A[i][col] == 0 {
			A[i][col] = 1
		} else {
			A[i][col] = 0
		}
	}
}
