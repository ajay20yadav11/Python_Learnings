package main

import (
	"fmt"
)			


func powerOfTwo(animated int) int {
	if animated == 0 {
		return 1
	} else {
		return animated * powerOfTwo(animated -1)
	}
}



func main() {
	fmt.Println(powerOfTwo(10))
}