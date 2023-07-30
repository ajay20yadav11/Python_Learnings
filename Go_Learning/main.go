package main

import (
	"fmt"
)


func main() {

	var myNumber int = 23
	defer fmt.Println("My number: ", myNumber)

	var ptr = &myNumber
	defer fmt.Println("Number: ", ptr)
	
}