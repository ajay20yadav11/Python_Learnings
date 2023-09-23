package main

import (
	"fmt"
)


// func _channel(c chan string) {

// 	// name := <- c
// 	fmt.Println("Hello,", <- c)
// }


func main () {
	c := make(chan string, 1)

	// go _channel(c)

	c <- "World"
	fmt.Println(<- c)
	defer close(c)
}