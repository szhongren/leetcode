package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(toLowerCase("HeLLo"))
}

func toLowerCase(str string) string {
	return strings.ToLower(str)
}
