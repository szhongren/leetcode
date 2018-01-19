package main

import "fmt"

func main() {
	fmt.Println(hammingDistance(1, 4))
}

func hammingDistance(x int, y int) int {
	var answer int
	for x > 0 || y > 0 {
		answer += (x & 1) ^ (y & 1)
		x >>= 1
		y >>= 1
	}
	return answer
}
