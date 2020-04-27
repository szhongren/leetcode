package main

import "fmt"

func main() {
	fmt.Println(numberOfLines(
		[]int{
			10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
			10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
		"abcdefghijklmnopqrstuvwxyz"))
}

func numberOfLines(widths []int, S string) []int {
	numLines := 0
	currentLine := 0
	for _, char := range S {
		currentLen := widths[char-rune('a')]
		if currentLine+currentLen > 100 {
			currentLine = currentLen
			numLines++
		} else {
			currentLine += currentLen
		}
	}
	return []int{numLines + 1, currentLine}
}
