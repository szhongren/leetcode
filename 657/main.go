package main

import "fmt"

func main() {
	fmt.Println(judgeCircle("UD"))
	fmt.Println(judgeCircle("LL"))
}

func judgeCircle(moves string) bool {
	var counts = map[string]int{
		"D": 0,
		"L": 0,
		"R": 0,
		"U": 0,
	}
	for _, char := range moves {
		counts[string(char)]++
	}
	return counts["D"] == counts["U"] && counts["R"] == counts["L"]
}
