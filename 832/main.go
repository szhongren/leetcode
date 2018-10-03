package main

import (
	"fmt"
)

func main() {
	image := [][]int{
		{1, 1, 0},
		{1, 0, 1},
		{0, 0, 0},
	}
	fmt.Println(flipAndInvertImage(image))
}

func flipAndInvertImage(A [][]int) [][]int {
	height := len(A)
	width := len(A[0])
	result := make([][]int, height)
	for i := 0; i < height; i++ {
		row := make([]int, width)
		for j := 0; j < width; j++ {
			row[j] = 1 - A[i][width-j-1]
		}
		result[i] = row
	}
	return result
}
