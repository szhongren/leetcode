package main

import "fmt"

func main() {
	fmt.Println(countPrimeSetBits(567, 607))
}

func countPrimeSetBits(L int, R int) int {
	bitCounts := []int{0}
	for len(bitCounts) < R+1 {
		tail := []int{}
		for _, v := range bitCounts {
			tail = append(tail, v+1)
		}
		bitCounts = append(bitCounts, tail...)
	}
	primes := map[int]bool{
		2: true,
	}
	checkedTo := 2
	result := 0
	for i := L; i <= R; i++ {
		currCount := bitCounts[i]
		if currCount != 2 && currCount%2 == 0 {
			continue
		}
		if currCount > checkedTo {
		loop:
			for j := checkedTo + 1; j <= currCount; j++ {
				for prime := range primes {
					if j%prime == 0 {
						continue loop
					}
				}
				primes[j] = true
			}
			checkedTo = currCount
		}
		if _, ok := primes[currCount]; ok {
			result++
		}
	}
	return result
}
