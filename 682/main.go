package main

import (
	"fmt"
	"strconv"
)

func main() {
	games := []string{"5", "2", "C", "D", "+"}
	fmt.Println(calPoints(games))
}

func calPoints(ops []string) int {
	parsedGames := []int{}
	result := 0
	for _, game := range ops {
		l := len(parsedGames)
		switch game {
		case "+":
			val := parsedGames[l-1] + parsedGames[l-2]
			parsedGames = append(parsedGames, val)
		case "D":
			val := parsedGames[l-1] * 2
			parsedGames = append(parsedGames, val)
		case "C":
			parsedGames = parsedGames[:l-1]
		default:
			val, _ := strconv.Atoi(game)
			parsedGames = append(parsedGames, val)
		}
	}
	for _, val := range parsedGames {
		result += val
	}
	return result
}
