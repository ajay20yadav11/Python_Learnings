package main

import (
	"fmt"
)




func main () {
					// This is Slice (List in Python) in Go

	// months := []int{1, 2, 3, 4, 5, 6, 7}
	// fmt.Println(months)
	// months = append(months, 8)
	// fmt.Println(months)
	// fmt.Println(months[1:3])

					// This is Tuple alike in Go, interface

	// months := []interface{"Jan", 2, true, 4}
	// fmt.Println(months[0]) 


					// This is Dict alike in Go, MAP

	monthsDigits := make(map[string]int)

	monthsDigits["January"] = 1
	monthsDigits["Feburary"] = 2
	monthsDigits["March"] = 3
	monthsDigits["April"] = 4

	fmt.Println(monthsDigits)

	for k, v := range monthsDigits {
		fmt.Println(k, v)
	}

	actualValue := []string{}
	actualValue = append(actualValue, "10")
	actualValue = append(actualValue, "20")
	actualValue = append(actualValue, "30")
	fmt.Printf("%T\n%v", actualValue, actualValue)
}