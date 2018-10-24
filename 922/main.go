package main

import "fmt"

func main() {
	fmt.Println(sortArrayByParityII([]int{4, 2, 5, 7}))
}

func sortArrayByParityII(A []int) []int {
	evenIndexes := []int{}
	oddIndexes := []int{}
	for i, v := range A {
		if v%2 == 0 {
			evenIndexes = append(evenIndexes, i)
		} else {
			oddIndexes = append(oddIndexes, i)
		}
	}
	result := make([]int, len(A), len(A))
	for i := 0; i < len(evenIndexes); i++ {
		result[i*2] = A[evenIndexes[i]]
		result[i*2+1] = A[oddIndexes[i]]
	}
	return result
}
