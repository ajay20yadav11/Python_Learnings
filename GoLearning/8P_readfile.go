package main

import (
	"fmt"
	"io/ioutil"
)


func readFile(filePath string) {
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(content))
}


func main() {
	fileName := "go.mod"
	readFile(fileName)
}