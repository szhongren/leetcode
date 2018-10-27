package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(complexNumberMultiply("1+1i", "1+1i"))
}

func complexNumberMultiply(a string, b string) string {
	real1, imag1 := complexNumberSeparate(a)
	real2, imag2 := complexNumberSeparate(b)
	realRes := real1*real2 - imag1*imag2
	imagRes := real1*imag2 + imag1*real2
	return fmt.Sprintf("%d+%di", realRes, imagRes)
}

func complexNumberSeparate(a string) (int, int) {
	values := strings.Split(a, "+")
	real, _ := strconv.Atoi(values[0])
	l := len(values[1])
	imag, _ := strconv.Atoi(values[1][:l-1])
	return real, imag
}
