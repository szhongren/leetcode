package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(reverseOnlyLetters("ab-cd"))
}

func reverseOnlyLetters(S string) string {
	if len(S) == 0 {
		return ""
	}
	var result strings.Builder
	runes := []rune(S)

	reversePointer := len(runes) - 1

	for reversePointer > -1 && !unicode.IsLetter(runes[reversePointer]) {
		reversePointer--
	}
	for _, char := range S {
		if unicode.IsLetter(char) {
			result.WriteRune(runes[reversePointer])
			reversePointer--
			for reversePointer > -1 && !unicode.IsLetter(runes[reversePointer]) {
				reversePointer--
			}
		} else {
			result.WriteRune(char)
		}
	}
	return result.String()
}
