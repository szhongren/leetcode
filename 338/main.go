package main

import "fmt"

func main() {
	fmt.Println(countBits(5))
}

func countBits(num int) []int {
	finalLen := num + 1
	counts := []int{0, 1}
	for len(counts) < finalLen {
		nextVals := []int{}
		for _, v := range counts {
			nextVals = append(nextVals, v+1)
		}
		counts = append(counts, nextVals...)
	}
	return counts[:finalLen]
}

/*
0 0
1 1
10 1
11 2
100 1
101 2
110 2
111 3
1000 1
1001 2
1010 2
1011 3
1100 2
1101 3
1110 3
1111 4
*/
