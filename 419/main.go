package main

import "fmt"

func main() {
	board := [][]byte{
		[]byte{'X', '.', '.', 'X'},
		[]byte{'.', '.', '.', 'X'},
		[]byte{'.', '.', '.', 'X'},
	}
	fmt.Println(countBattleships(board))
}

func countBattleships(board [][]byte) int {
	/*
		going from top left, I scan through
		every time I see an X it's either a new ship or one I've already seen before
	*/
	count := 0
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			curr := board[i][j]
			if curr == 'X' {
				if i != 0 && board[i-1][j] == 'X' {
					continue
				} else if j != 0 && board[i][j-1] == 'X' {
					continue
				} else {
					count++
				}
			}
		}
	}
	return count
}
