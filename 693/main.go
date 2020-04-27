package main

import "fmt"

func main() {
	for i := 0; i < 15; i++ {
		fmt.Println(i, hasAlternatingBits(i))
	}
}

func hasAlternatingBits(n int) bool {
	currentBit := n % 2
	n /= 2
	for n > 0 {
		if currentBit == n%2 {
			return false
		}
		n /= 2
		switch currentBit {
		case 0:
			currentBit = 1
		case 1:
			currentBit = 0
		}
	}
	return true
}
