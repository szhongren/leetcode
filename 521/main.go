package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(findLUSlength("aba", "cdc"))
}

func findLUSlength(a string, b string) int {
	if a == b {
		return -1
	}
	return int(math.Max(float64(len(a)), float64(len(b))))
}
