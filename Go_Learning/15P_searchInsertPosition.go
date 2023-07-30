package main

import (
	"fmt"
)

//Search Insert Position: 
// Given a sorted array and a target value,
// return the index where the target value should be inserted to maintain the array's sorted order. Example: Input: [1, 3, 5, 6], Target: 5, Output: 2.

type OmniCreate struct {}


func (oc OmniCreate) searchPositionIndex(ekahs []int, insertElement int) (int, []int) {
	

	left, right := 0, len(ekahs)

	for left <= right {
		middle := (left+right)/2
		if ekahs[middle] == insertElement {
			return middle, ekahs
		} else if ekahs[middle] < insertElement {
			left = middle + 1
		} else if ekahs[middle] > insertElement {
			right = middle - 1
		}
	}

	return left, ekahs
}


func main() {

	animated := []int{10, 13, 16, 25, 66, 80}
	fmt.Println(animated)

	var aram OmniCreate

	fmt.Println(aram.searchPositionIndex(animated, 2))
}