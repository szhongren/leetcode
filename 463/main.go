package main

import "fmt"

func main() {
	matrix := [][]int{
		[]int{0, 1, 0, 0},
		[]int{1, 1, 1, 0},
		[]int{0, 1, 0, 0},
		[]int{1, 1, 0, 0},
	}
	fmt.Println(islandPerimeter(matrix))
}

func islandPerimeter(grid [][]int) int {
	totalSides := 0
	repeatedSides := 0
	for i, row := range grid {
		for j, cell := range row {
			if cell == 1 {
				if i != 0 && grid[i-1][j] == 1 {
					repeatedSides++
				}
				if j != 0 && grid[i][j-1] == 1 {
					repeatedSides++
				}
			}
			totalSides += cell * 4
		}
	}
	return totalSides - 2*repeatedSides
}
