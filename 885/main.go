package main

import "fmt"

func main() {
	fmt.Println(spiralMatrixIII(5, 6, 1, 4))
}

type direction struct {
	x, y int
}

func spiralMatrixIII(R int, C int, r0 int, c0 int) [][]int {
	directions := []direction{
		direction{1, 0},
		direction{0, 1},
		direction{-1, 0},
		direction{0, -1},
	}
	pathLengths := []int{1, 1}
	unvisited := R * C
	results := [][]int{}
	for currPath := 0; unvisited > 0; currPath++ {
		l := len(pathLengths)
		if l == currPath+1 {
			pathLengths = append(pathLengths, pathLengths[l-1]+1, pathLengths[l-1]+1)
		}
		for move := 0; move < pathLengths[currPath]; move++ {
			if r0 >= 0 && r0 < R && c0 >= 0 && c0 < C {
				results = append(results, []int{r0, c0})
				unvisited--
			}
			currDir := directions[currPath%4]
			r0 += currDir.y
			c0 += currDir.x
		}
	}
	return results
}
