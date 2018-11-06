package main

import (
	"fmt"
	"sort"
)

func main() {
	people := [][]int{
		[]int{7, 0},
		[]int{4, 4},
		[]int{7, 1},
		[]int{5, 0},
		[]int{6, 1},
		[]int{5, 2},
	}
	fmt.Println(reconstructQueue(people))
}

type person struct {
	height, tallerInFront int
}

type personSorter []person

func (p personSorter) Len() int {
	return len(p)
}

func (p personSorter) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func (p personSorter) Less(i, j int) bool {
	if p[i].height > p[j].height {
		return true
	} else if p[i].height == p[j].height {
		return p[i].tallerInFront < p[j].tallerInFront
	} else {
		return false
	}
}

func makePersonList(people [][]int) []person {
	result := []person{}
	for _, p := range people {
		result = append(result, person{p[0], p[1]})
	}
	return result
}

func reconstructQueue(people [][]int) [][]int {
	result := [][]int{}
	personList := makePersonList(people)
	sort.Sort(personSorter(personList))

	currentH := -1
	tempArray := []person{}
	for i, p := range personList {
		if currentH != p.height {
			// do something diff
			for _, currP := range tempArray {
				indexToInsertAt := currP.tallerInFront
				result = append(result, []int{}) // just add space
				copy(result[indexToInsertAt+1:], result[indexToInsertAt:])
				result[indexToInsertAt] = []int{currP.height, currP.tallerInFront}
			}
			tempArray = []person{p}
			currentH = p.height

		} else {
			tempArray = append(tempArray, p)
			continue
		}
	}
	for _, currP := range tempArray {
		indexToInsertAt := currP.tallerInFront
		result = append(result, []int{}) // just add space
		copy(result[indexToInsertAt+1:], result[indexToInsertAt:])
		result[indexToInsertAt] = []int{currP.height, currP.tallerInFront}
	}
	return result
}
