package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(findWords([]string{"Hello", "Alaska", "Dad", "Peace"}))
}

func findWords(words []string) []string {
	firstRow := "qwertyuiop"
	secondRow := "asdfghjkl"
	thirdRow := "zxcvbnm"
	result := []string{}
	for _, word := range words {
		lowerWord := strings.ToLower(word)
		if strings.IndexByte(firstRow, lowerWord[0]) != -1 {
			if inRow(lowerWord, firstRow) {
				result = append(result, word)
			}
		} else if strings.IndexByte(secondRow, lowerWord[0]) != -1 {
			if inRow(lowerWord, secondRow) {
				result = append(result, word)
			}
		} else if strings.IndexByte(thirdRow, lowerWord[0]) != -1 {
			if inRow(lowerWord, thirdRow) {
				result = append(result, word)
			}
		}
	}
	return result
}

func inRow(word string, row string) bool {
	for _, char := range word {
		if strings.IndexRune(row, char) == -1 {
			return false
		}
	}
	return true
}
