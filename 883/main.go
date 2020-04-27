package main

import "fmt"

func main() {
	grid := [][]int{
		[]int{1, 2},
		[]int{3, 4},
	}
	fmt.Println(projectionArea(grid))
}

func projectionArea(grid [][]int) int {
	topArea := 0
	sideArea := 0
	frontAreaMaxes := map[int]int{}
	for _, row := range grid {
		rowMax := 0
		for i, val := range row {
			if val > 0 {
				topArea++
			}
			if val > rowMax {
				rowMax = val
			}
			if _, ok := frontAreaMaxes[i]; !ok {
				frontAreaMaxes[i] = val
			} else {
				if val > frontAreaMaxes[i] {
					frontAreaMaxes[i] = val
				}
			}
		}
		sideArea += rowMax
	}
	result := 0
	for _, val := range frontAreaMaxes {
		result += val
	}
	return topArea + sideArea + result
}
