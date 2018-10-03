package main

import (
	"fmt"
)

func main() {
	fmt.Println(findAndReplacePattern([]string{"abc", "deq", "mee", "aqq", "dkd", "ccc"}, "abb"))
}

func findAndReplacePattern(words []string, pattern string) []string {
	result := []string{}
	for _, word := range words {
		if patternMatch(word, pattern) {
			result = append(result, word)
		}
	}
	return result
}

func patternMatch(word string, pattern string) bool {
	patternToWord := make(map[byte]byte, len(pattern))
	wordToPattern := make(map[byte]byte, len(pattern))
	for i := range pattern {
		if _, ok := patternToWord[pattern[i]]; !ok {
			patternToWord[pattern[i]] = word[i]
		}
		if _, ok := wordToPattern[word[i]]; !ok {
			wordToPattern[word[i]] = pattern[i]
		}
		if patternToWord[pattern[i]] != word[i] || wordToPattern[word[i]] != pattern[i] {
			return false
		}
	}
	return true
}
