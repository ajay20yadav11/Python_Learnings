// 
// write this hackerrank question in Go, give solution here  below

// A grocery store is selling apples by count.
// They want to set the same price for each apple that they sell.
// They received total N apples of different weight from the farm.

// To be able to set the same price for each apple, they need to select only those set of apples where the weight different between the larget and the smallest apple is not more than K.
// Given the range K, what is the maximum number of apples they can select from the N apples.

// Input Format
// Locked stub code in the editor reads the following input from stdin and passes it to the function:
// The first line contains the range K.
// The second line contains the number of apples N.
// The subsequent lines contain size of each apple, one per line.

// Output Fromat

// The Function must return an interger specifying the maximum number of apples that can be selected from the input set of N apples which are all within a weight range of maximum K amoung each other

// Sample input

// 2
// 8
// 4
// 2
// 6
// 100
// 101
// 101
// 110
// 102

// Sample output 

// 4

// Explanation 0

// The above input specifies a maximum wight difference range of 2, and total 8 apples as input followed by their weights

// 3 different subsets are possible above which are all within weight different of 2:
// - 2, 4
// - 4, 6
// - 100, 101, 101, 102

// the maximum number of apples (the larget subset) is hence 4 100, 101, 101, 102

package main

import (
	"fmt"
	"sort"
)


type ApplesBuySell struct {}


func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func (a *ApplesBuySell) bruteForceMaximumApples(appleStock []int) ([]int, int) {
	k := appleStock[0]
	totallengths := appleStock[1]
	appleStock = appleStock[2:]
	sort.Ints(appleStock)
	maximumApples := []int{}
	maximumCount := 0

	for i := 0; i < totallengths; i ++ {
		counter := 1
		for j := i+1; j < totallengths; j ++ {
			if appleStock[j] - appleStock[i] <= k {
				counter += 1
			}
		}
		if counter > maximumCount {
			maximumCount = counter
			maximumApples = appleStock[i:i+counter]
		}
	}
	return maximumApples, maximumCount
}

func (a *ApplesBuySell) dynamicProgrammingMaximumApples(appleStock []int) ([]int, int) {
	k := appleStock[0]
	totallengths := appleStock[1]
	appleStock = appleStock[2:]
	sort.Ints(appleStock)
	maximumApples := []int{}

	dp := make([]int, totallengths)
	dp[0] = 1

	for i := 1; i < totallengths; i ++ {
		dp[i] = 1
		for j := i+1; j < totallengths; j ++ {
			if appleStock[j] - appleStock[i] <= k {
				dp[i] = max(dp[i], dp[i-1]+1)
			}
		}
	}
		
	maxCount := 0

	for i := 0; i < totallengths; i ++ {
		maxCount = max(maxCount, dp[i])
	}

	for i := 1; i < totallengths; i ++ {
		if dp[i] > dp[i-1] && dp[i] == maxCount {
			maximumApples = appleStock[i-2:i+maxCount-2]
		}
	}
	return maximumApples, maxCount
}


func main() {
	appleStock := []int{2, 8, 4, 2, 6, 100, 101, 101, 110, 102}
	apples := &ApplesBuySell{}
	fmt.Println(apples.bruteForceMaximumApples(appleStock))
	fmt.Println(apples.dynamicProgrammingMaximumApples(appleStock))
}