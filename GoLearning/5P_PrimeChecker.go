package main

import (
	"fmt"
)


func primeChecker(animated int) {

	for i := 0; i <= animated; i++ {
		if i % 2 == 0 {
			fmt.Println(i)
		}
	}
}


func main() {
	primeChecker(10)
}