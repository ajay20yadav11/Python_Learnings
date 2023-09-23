package main


import (
	"fmt"
)

func checkUnevenBrackets(rawData string) bool {
	bracketDigest := map[string]string{
		"}": "{",
		")": "(",
		"]": "[",
	}
	stackBrackets := []string{}
	for _, chrac := range rawData {
		chr := string(chrac)
		if chr == "{" || chr == "[" || chr == "(" {
			stackBrackets = append(stackBrackets, chr)
		} else if chr == "}" || chr == "]" || chr == ")" {
			if len(stackBrackets) == 0 || stackBrackets[len(stackBrackets)-1] != bracketDigest[chr] {
				return false
			}
			stackBrackets = stackBrackets[:len(stackBrackets)-1]
		}
	}
	return true
}


func main() {
	inputRawData := []string{
	"(hello [world])(!)",
	"(coder)[byte)]",
	"(c([od]er)) b(yt[e])",
	}
	isUneven := []bool{}
	for _, bracket := range inputRawData {
		isUneven = append(isUneven, checkUnevenBrackets(bracket))
	}
	fmt.Println(isUneven)
}



