package main

import "fmt"

func main() {
	fmt.Println(partitionLabels("ababcbacadefegdehijhklij"))
}

type span struct {
	min, max int
}

func partitionLabels(S string) []int {
	letterSpans := map[rune]span{}
	for i, char := range S {
		if spanI, ok := letterSpans[char]; ok {
			letterSpans[char] = span{spanI.min, i}
		} else {
			letterSpans[char] = span{i, i}
		}
	}

	result := []int{}
	front := 0
	end := 0
	for i := 0; i < len(S); i++ {
		currentChar := rune(S[i])
		if i > end {
			result = append(result, end-front+1)
			front = i
			end = letterSpans[currentChar].max
		} else {
			if letterSpans[currentChar].max > end {
				end = letterSpans[currentChar].max
			}
		}
	}
	result = append(result, end-front+1)
	return result
}
