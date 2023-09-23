package main

import (
	"fmt"
)



func findFibonacci(animated int) int {
	if animated == 0 || animated == 1 {
		return 1
	}
	return findFibonacci(animated - 1) + findFibonacci(animated - 2)
}



func main() {
	fmt.Print("Enter Number: ")
	var numb int
	fmt.Scanf("%d", &numb)
	fmt.Println(numb)
	fmt.Print(findFibonacci(numb))
}