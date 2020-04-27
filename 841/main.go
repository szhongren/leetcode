package main

import "fmt"

func main() {
	rooms := [][]int{
		[]int{1, 3},
		[]int{3, 0, 1},
		[]int{2},
		[]int{0},
	}
	fmt.Println(canVisitAllRooms(rooms))
}

func canVisitAllRooms(rooms [][]int) bool {
	visited := []bool{}
	for i := 0; i < len(rooms); i++ {
		visited = append(visited, false)
	}
	queue := []int{0}
	for len(queue) != 0 {
		currRoom := queue[0]
		queue = queue[1:]
		for _, key := range rooms[currRoom] {
			if !visited[key] {
				queue = append(queue, key)
			}
		}
		visited[currRoom] = true
	}
	for _, val := range visited {
		if !val {
			return false
		}
	}
	return true
}
