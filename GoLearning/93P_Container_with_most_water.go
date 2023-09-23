package main

import (
    "fmt"
)

// """
// Given an array of non-negative integers height, where height[i] represents the height of the line at position i,
// find two lines, which together with the x-axis, forms a container such that the container contains the most water.
// Example:
// Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
// Output: 49
// """


type OmniCreate struct{}

func min(anim int, bnim int) int {

    if anim < bnim {
        return anim
    } 
    return bnim
}

func max(anim int, bnim int) int {
    if anim > bnim {
        return anim
    }
    return bnim
}

func (oc OmniCreate) MaxContainer(ekahs []int) int {

    maxContainer := 0
    left, right := 0, len(ekahs) - 1
    // Formulae: Area = min(1, 7)*(index of 1 - index of 7)
    for left <= right {
        minOfTwo := min(ekahs[left], ekahs[right])
        distanceOfTwo := right - left
        currentArea := minOfTwo * distanceOfTwo
        maxContainer = max(currentArea, maxContainer)

        if ekahs[left] < ekahs[right] {
            left ++
        } else {
            right --
        }
    }
    return maxContainer

}


func main() {
    var create OmniCreate
    animated := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
    fmt.Println(create.MaxContainer(animated))
}