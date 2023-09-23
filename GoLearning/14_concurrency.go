package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	anim, bnim int
	wg sync.WaitGroup
)


func foo () {
	defer wg.Done()
	for anim = 0; anim < 10 ; anim ++ {
		fmt.Println(anim)
	}
}

func bar () {
	defer wg.Done()		
	for bnim = 0; bnim < 10 ; bnim++ {
		fmt.Println(bnim)
	}
}


func main () {

	fmt.Println("OS", runtime.GOOS)
	fmt.Println("ARCH", runtime.GOARCH)
	fmt.Println("CPU", runtime.NumCPU())
	fmt.Println("Goroutines", runtime.NumGoroutine())

	wg.Add(1)
	go foo()
	wg.Add(1)
	bar()
	
	fmt.Println("OS", runtime.GOOS)
	fmt.Println("ARCH", runtime.GOARCH)
	fmt.Println("CPU", runtime.NumCPU())
	fmt.Println("Goroutines", runtime.NumGoroutine())
	wg.Wait()
}