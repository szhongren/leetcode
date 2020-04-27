package main

import (
	"bytes"
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(fizzBuzz(15))
}

func fizzBuzz(n int) []string {
	result := []string{}
	for val := 1; val <= n; val++ {
		var str bytes.Buffer
		if val%3 == 0 {
			str.WriteString("Fizz")
		}
		if val%5 == 0 {
			str.WriteString("Buzz")
		}
		if len(str.String()) == 0 {
			str.WriteString(strconv.Itoa(val))
		}
		result = append(result, str.String())
	}
	return result
}
