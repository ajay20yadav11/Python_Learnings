package main

import (
	"fmt"
	"encoding/json"
)


type courses struct {
	Name string
	Price int
	Platform string
	Password string
	Tags []string
}

func EncodedJson() {
	lcoCourses := []courses{
		{"ReachJS Bootcamp", 299, "LearnCodeOnline.in", "abc123", []string{"web-dev", "js"}},
		{"Python Bootcamp", 299, "LearnCodeOnline.in", "pyc123", []string{"full-stack", "js"}},
		{"Go Bootcamp", 299, "LearnCodeOnline.in", "gec123", nil},
	}

	// package this into JSON data

	finalJson, err := json.MarshalIndent(lcoCourses, "", "\t")
	if err != nil {
		panic(err)
	}
	// var mapValue []map[string]interface{}
	fmt.Printf(string(finalJson))
	// mapValue = finalJson()[0]
	// fmt.Println(mapValue)

	checkValid := json.Valid(finalJson)
	print(checkValid)
}

func DecodedJson() {
	jsonDataFrame := []byte(`
		[
	        {
	                "Name": "ReachJS Bootcamp",
	                "Price": 299,
	                "Platform": "LearnCodeOnline.in",
	                "Password": "abc123",
	                "Tags": [
	                        "web-dev",
	                        "js"
	                ]
	        },
	        {
	                "Name": "Python Bootcamp",
	                "Price": 299,
	                "Platform": "LearnCodeOnline.in",
	                "Password": "pyc123",
	                "Tags": [
	                        "full-stack",
	                        "js"
	                ]
	        },
	        {
	                "Name": "Go Bootcamp",
	                "Price": 299,
	                "Platform": "LearnCodeOnline.in",
	                "Password": "gec123",
	                "Tags": null
	        }
        ]
    `)
    checkValid := json.Valid(jsonDataFrame)
    fmt.Println(checkValid)
    var decodedValue map[string]interface{}
    json.Unmarshal(jsonDataFrame, &decodedValue)
    // fmt.Printf("%s\n", decodedValue)
    for _, v := range decodedValue {
    	fmt.Printf("%#v\n", v)
    }
}


func main() {
	fmt.Println("Welcome to JSON lecture.")
	EncodedJson()
	DecodedJson()
}