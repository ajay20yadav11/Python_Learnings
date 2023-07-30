package main

import (
	"fmt"
)


func findSumOfDigit(animated int) int {

	if animated == 0 || animated == 1 {
		return 1
	}

	return findSumOfDigit(animated / 10) + (animated % 10)

}


func main() {
	fmt.Print("Enter the number to sum: ")
	var numb int
	fmt.Scanln(&numb)
	fmt.Println(findSumOfDigit(numb))
}