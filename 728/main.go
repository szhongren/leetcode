package main

import "fmt"

func main() {
	fmt.Println(selfDividingNumbers(1, 22))
}

func selfDividingNumbers(left int, right int) []int {
	result := []int{}
	for i := left; i <= right; i++ {
		if selfDividingNumber(i) {
			result = append(result, i)
		}
	}
	return result
}

func selfDividingNumber(number int) bool {
	for decrementor := number; decrementor > 0; decrementor /= 10 {
		digit := decrementor % 10
		if digit == 0 || number%digit != 0 {
			return false
		}
	}
	return true
}
