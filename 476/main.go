package main

import "fmt"

func main() {
	fmt.Println(findComplement(5))
}

func findComplement(num int) int {
	result := 0
	curr := 1
	for num > 0 {
		bit := num % 2
		if bit == 1 {
			bit = 0
		} else {
			bit = 1
		}
		result += bit * curr
		num /= 2
		curr *= 2
	}
	return result
}
