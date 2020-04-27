package main

import (
	"fmt"
)

func main() {
	fmt.Println(minAddToMakeValid("()))(("))
}

func minAddToMakeValid(S string) int {
	openCount := 0
	unclosedCount := 0
	for _, char := range S {
		if char == rune('(') {
			openCount++
		}
		if char == rune(')') {
			if openCount == 0 {
				unclosedCount++
			} else {
				openCount--
			}
		}
	}
	return openCount + unclosedCount
}
