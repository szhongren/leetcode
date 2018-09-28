package main

import (
	"fmt"
)

func main() {
	fmt.Println(numJewelsInStones("aA", "aAAbbbb"))
}

func numJewelsInStones(J string, S string) int {
	jewels := make(map[int32]bool)
	for _, char := range J {
		jewels[char] = true
	}
	numJewels := 0
	for _, char := range S {
		if _, ok := jewels[char]; ok {
			numJewels++
		}
	}
	return numJewels
}
