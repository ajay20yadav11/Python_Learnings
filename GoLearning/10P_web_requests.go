package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)


const url = "https://linkedin.com/in/ajaylnyadav"


func main() {
	fmt.Println("LCO Web Request")
	response, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()

	databyte, _ := ioutil.ReadAll(response.Body)
	fmt.Println(string(databyte))
}