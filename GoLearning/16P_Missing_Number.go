package main

import (
	"fmt"
)

// Problem: "Find the missing number in a sorted list with consecutive integers from 1 to N, where N is the length of the list. The list contains N-1 unique integers."

// Example:
// Input: [1, 2, 4, 5, 6, 7, 8]
// Output: 3

func Sum(animated []int) int {
	sum := 0
	for _, anim := range animated {
		sum += anim
	}
	return sum
}

func makeRange(start, end int) []int {
	r := make([]int, end-start+1)
	for i := range r {
		r[i] = start + i
	}
	return r
}

func missingNumber(ekahs []int) ([]int, []int) {
	left, right := 0, len(ekahs)-1
	middle := (left + right) / 2
	numberMissing := []int{}

	if Sum(ekahs[left:right+1]) == Sum(makeRange(ekahs[left], ekahs[right-1])) {
		return numberMissing, ekahs
	}

	for left <= middle {
		if Sum(ekahs[left:middle]) != Sum(makeRange(ekahs[left], ekahs[middle-1])) {
			num := (Sum(makeRange(ekahs[left], ekahs[middle-1])) - Sum(ekahs[left:middle]))
			numberMissing = append(numberMissing, num)
			left++
		} else {
			break
		}
	}

	for middle <= right {
		if Sum(makeRange(ekahs[middle+1], ekahs[right])) != Sum(ekahs[middle+1 : right+1]) {
			num := (Sum(makeRange(ekahs[middle+1], ekahs[right])) - Sum(ekahs[middle+1:right+1]))
			numberMissing = append(numberMissing, num)
			right--
		} else {
			break
		}
	}

	return numberMissing, ekahs
}

func main() {
	missingNumbers, originalList := missingNumber([]int{1, 2, 4, 6, 8})
	fmt.Println("Missing Numbers:", missingNumbers)
	fmt.Println("Original List:", originalList)
}
