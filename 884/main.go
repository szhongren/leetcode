package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(uncommonFromSentences("this apple is sweet", "this apple is sour"))
}

func uncommonFromSentences(A string, B string) []string {
	words := append(strings.Split(A, " "), strings.Split(B, " ")...)
	counts := map[string]int{}
	result := []string{}
	for _, word := range words {
		if _, ok := counts[word]; !ok {
			counts[word] = 1
		} else {
			counts[word]++
		}
	}
	for word, count := range counts {
		if count == 1 {
			result = append(result, word)
		}
	}
	return result
}
