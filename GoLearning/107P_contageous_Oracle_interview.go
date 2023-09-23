// Find contageous and non contageous
// for e.g. input = 1, 2, 3, 4, 6, 7, 9, 10, 11, 12
// output= 1-4, 6, 7, 9-12

package main

import (
	"fmt"
)

type CheckContageous struct{}

func (a *CheckContageous) filterContinuity(example []int) string {
	first_window := example[0]
	last_window := example[0]

	var output string

	for value := 0; value < len(example)-1; value++ {
		if example[value+1] == example[value]+1 {
			last_window = example[value+1]
		} else {
			if first_window == last_window {
				output += fmt.Sprintf("%d, ", first_window)
			} else {
				output += fmt.Sprintf("%d-%d, ", first_window, last_window)
			}
			first_window = example[value+1]
		}
	}
	// Handle the last window
	if first_window == last_window {
		output += fmt.Sprintf("%d", first_window)
	} else {
		output += fmt.Sprintf("%d-%d", first_window, last_window)
	}
	return output
}

func main() {
	given_example := []int{1, 2, 3, 4, 6, 7, 9, 10, 11, 12}
	filter := CheckContageous{}
	fmt.Println(filter.filterContinuity(given_example))
}
