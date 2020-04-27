package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(reverseString("Hello"))
}

func reverseString(s string) string {
	var result bytes.Buffer
	for i := len(s) - 1; i > -1; i-- {
		result.WriteByte(s[i])
	}
	return result.String()
}
