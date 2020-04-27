package main

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(binaryGap(i))
	}
}

func binaryGap(N int) int {
	if N == 0 {
		return 0
	}
	for ; N%2 == 0; N /= 2 {
	}
	if N == 1 {
		return 0
	}
	longestDist := 0
	currDist := 0
	for ; N != 1; N /= 2 {
		bit := N % 2
		switch bit {
		case 1:
			if currDist > longestDist {
				longestDist = currDist
			}
			currDist = 0
		case 0:
			currDist++
		}
	}
	if currDist > longestDist {
		longestDist = currDist
	}
	return longestDist + 1
}
