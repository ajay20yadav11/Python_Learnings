package main

import (
	"fmt"
)


func main() {
	userch := make(chan string, 4)

	userch <- "anim"
	user := <- userch
	fmt.Println(user, &user)
	fmt.Println(userch, &userch)


	userch <- "bnim"
	vbser := <- userch
	fmt.Println(vbser, &vbser)
	fmt.Println(userch, &userch)

	userch <- "cnim"
	wuser := <- userch
	fmt.Println(wuser, &wuser)
	fmt.Println(userch, &userch)


}
