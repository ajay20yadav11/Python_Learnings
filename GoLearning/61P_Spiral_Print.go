package main

import (
    "fmt"
)


func SpiralPrint(ekahs [][]int) {

    for _, anim := range ekahs {
            fmt.Println(anim)
    }

    top, bottom, left, right := 0, len(ekahs) - 1, 0, len(ekahs) - 1
    fmt.Println(left, right, top, bottom)
    fmt.Println("\n\n")
    // for anim := range (len(ekahs)) {
    //     for bnim := range(len(ekahs[anim])){
    //         fmt.Println(ekahs[anim][bnim])
    //     }
    // }

    for left <= right && top <= bottom {

        for anim := left; anim <= right; anim ++ {
            fmt.Println(ekahs[top][anim])
        }
        top ++

        for anim := top; anim <= bottom; anim++ {
            fmt.Println(ekahs[anim][right])
        }
        right--

        if top <= bottom {
            for anim := right; anim >= left; anim-- {
                fmt.Println(ekahs[bottom][anim])
            }
            bottom--
        }

        // Print the leftmost column (in reverse)
        if left <= right {
            for anim := bottom; anim >= top; anim-- {
                fmt.Println(ekahs[anim][left])
            }
            left++
        }

    }
    
}



func main() {

    exp := [][]int{
                    {1, 2, 3},
                    {4, 5, 6}, 
                    {7, 8, 9},
    }

    SpiralPrint(exp)


}