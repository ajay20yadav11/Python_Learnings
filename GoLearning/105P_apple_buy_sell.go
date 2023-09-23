package main

import (
	"fmt"
)


func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

type Apples struct {}

// Find the maximum profit considering minimum price
func (a *Apples) SlidingAppleBuySell(apples []int) int {
	maxProfit := 0
	minPrice := apples[0]

	for _, apple := range apples {
		if apple > minPrice {
			maxProfit = max(maxProfit, apple - minPrice)
		} else {
			minPrice = apple
		}
	}
	return maxProfit
}

func (a *Apples) DynAppleBuySell(apples []int) int {
	dp := make([]int, len(apples))
	dp[0] = 0

	for currentIndex, _ := range apples {
		if currentIndex > 0 {
			dp[currentIndex] = max(dp[currentIndex-1], dp[currentIndex-1] + apples[currentIndex] - apples[currentIndex-1])
		}
	}
	return dp[len(apples)-1]
}

func (a* Apples) PotentialProfitBuySell(apples []int) int {
	maxProfit := 0
	for currentIndex :=1; currentIndex < len(apples); currentIndex ++ {
		potentialProfit := apples[currentIndex] - apples[currentIndex - 1]
		if  potentialProfit > 0 {
			maxProfit += potentialProfit
		}
	}
	return maxProfit
}


func main() {
	applesInstances := &Apples{}
	inStock := []int{7, 1, 5, 3, 6, 4, 13}
	winApples := applesInstances.SlidingAppleBuySell(inStock)
	fmt.Println("Using Sliding Window Approach ->", winApples)
	fmt.Println("Using Dynamic Progammic Approach ->", applesInstances.DynAppleBuySell(inStock))
	fmt.Println("Using Potential Profit Appraoch ->", applesInstances.PotentialProfitBuySell(inStock))
}