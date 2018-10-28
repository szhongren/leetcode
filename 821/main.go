package main

import "fmt"

func main() {
	fmt.Println(shortestToChar("loveleetcode", 'e'))
}

func shortestToChar(S string, C byte) []int {
	charPositions := []int{}
	for i, char := range S {
		if char == rune(C) {
			charPositions = append(charPositions, i)
		}
	}
	charPositions = append(charPositions, len(S)*3)
	currClosestC := 0
	result := []int{}
	for i, char := range S {
		distToCurr := charPositions[currClosestC] - i
		if distToCurr < 0 {
			distToCurr *= -1
		}
		distToNext := charPositions[currClosestC+1] - i
		if distToNext < 0 {
			distToNext *= -1
		}
		if distToNext < distToCurr {
			currClosestC++
			distToCurr = distToNext
		}
		result = append(result, distToCurr)
	}
	return result
}
