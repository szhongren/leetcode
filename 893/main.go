package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println(numSpecialEquivGroups([]string{
		"abcd",
		"cdab",
		"adcb",
		"cbad",
	}))
}

type signature struct {
	even, odd map[byte]int
}

func numSpecialEquivGroups(A []string) int {
	signatures := []signature{}
outerloop:
	for _, word := range A {
		currSignature := signature{
			map[byte]int{},
			map[byte]int{},
		}
		for i := 0; i < len(word); i += 2 {
			if _, ok := currSignature.even[word[i]]; !ok {
				currSignature.even[word[i]] = 1
			} else {
				currSignature.even[word[i]]++
			}
		}
		for i := 1; i < len(word); i += 2 {
			if _, ok := currSignature.odd[word[i]]; !ok {
				currSignature.odd[word[i]] = 1
			} else {
				currSignature.odd[word[i]]++
			}
		}
		for _, sig := range signatures {
			if reflect.DeepEqual(sig, currSignature) {
				continue outerloop
			}
		}
		signatures = append(signatures, currSignature)
	}
	return len(signatures)
}
