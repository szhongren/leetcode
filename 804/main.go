package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(uniqueMorseRepresentations([]string{"gin", "zen", "gig", "msg"}))
}

func uniqueMorseRepresentations(words []string) int {
	morseKey := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	seen := map[string]bool{}
	for _, word := range words {
		var morse strings.Builder
		for _, char := range word {
			morse.WriteString(morseKey[char-'a'])
		}
		morseString := morse.String()
		if _, ok := seen[morseString]; !ok {
			seen[morseString] = true
		}
	}
	return len(seen)
}
