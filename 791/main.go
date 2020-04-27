package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(customSortString("cba", "abcd"))
}

func customSortString(S string, T string) string {
	counts := map[rune]int{}
	for _, char := range T {
		if _, ok := counts[char]; !ok {
			counts[char] = 1
		} else {
			counts[char]++
		}
	}
	var result bytes.Buffer
	for _, char := range S {
		if count, ok := counts[char]; ok {
			for i := 0; i < count; i++ {
				result.WriteRune(char)
			}
			delete(counts, char)
		}
	}
	for char, count := range counts {
		for i := 0; i < count; i++ {
			result.WriteRune(char)
		}
	}
	return result.String()
}
