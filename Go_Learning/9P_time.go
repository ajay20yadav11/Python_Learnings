package main

import (
	"fmt"
	"time"
)

func main() {
// 	fmt.Println("Welcome to time study of golang")
// 	presentTime := time.Now()
// 	fmt.Println(presentTime.Format("01-02-2006 15:04 Monday"))
// 	createdDate := time.Date(2020, time.March, 10, 23, 23, 0, 0, time.UTC)
// 	fmt.Println(createdDate.Format("01-02-2006 Monday"))

	endTime := "2072/07/09 14:14:14"
	givenTime, err := time.Parse("2006/01/02 15:04:05", endTime)
	if err != nil {
		fmt.Println("Error parsing the given time:", err)
		return
	}

	// Get the current time
	currentTime := time.Now()

	// Calculate the difference between the given time and current time
	diff := currentTime.Sub(givenTime)
	if diff >= (50 * 365 * 24 * time.Hour) {
		fmt.Println("OKAY")
	} else {
		fmt.Println("ERROR")
	}
}
