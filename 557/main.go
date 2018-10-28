package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(reverseWords("Let's take LeetCode contest"))
}

func reverseWords(s string) string {
	spaces := []int{-1}
	for i, char := range s {
		if char == rune(' ') {
			spaces = append(spaces, i)
		}
	}
	spaces = append(spaces, len(s))
	var result bytes.Buffer
	for i := 1; i < len(spaces); i++ {
		start := spaces[i-1]
		end := spaces[i]
		result.WriteString(reverseWord(s, start, end))
		result.WriteByte(' ')
	}
	return result.String()[0:len(s)]
}

func reverseWord(s string, start int, end int) string {
	var result bytes.Buffer
	for i := end - 1; i > start; i-- {
		result.WriteByte(s[i])
	}
	return result.String()
}
