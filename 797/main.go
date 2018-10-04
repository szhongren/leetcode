package main

import (
	"fmt"
)

func main() {
	graph := [][]int{
		[]int{3, 1},
		[]int{4, 6, 7, 2, 5},
		[]int{4, 6, 3},
		[]int{6, 4},
		[]int{7, 6, 5},
		[]int{6},
		[]int{7},
		[]int{},
	}
	fmt.Println(allPathsSourceTarget(graph))
}

type Stack []int

func (st Stack) push(val int) []int {
	return append(st, val)
}

func (st Stack) pop() (Stack, int) {
	l := len(st)
	if l == 0 {
		return st, 0
	}
	return st[:l-1], st[l-1]
}

func (st Stack) empty() bool {
	return len(st) == 0
}

func allPathsSourceTarget(graph [][]int) [][]int {
	result := make([][]int, 0, 0)
	allPathsSourceTargetHelper(0, graph, []int{0}, &result)
	return result
}

func allPathsSourceTargetHelper(curr int, graph [][]int, path []int, allPaths *[][]int) {
	end := len(graph) - 1
	if curr == end {
		*allPaths = append(*allPaths, path)
	} else {
		for _, nextNode := range graph[curr] {
			// deep copy because otherwise later paths overwrite earlier paths
			nextPath := []int{}
			for _, pathNode := range path {
				nextPath = append(nextPath, pathNode)
			}
			nextPath = append(nextPath, nextNode)
			allPathsSourceTargetHelper(nextNode, graph, nextPath, allPaths)
		}
	}
}
