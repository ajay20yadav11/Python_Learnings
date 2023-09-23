package main

import (
    "regexp"
    "fmt"
)

func main() {
    var re = regexp.MustCompile(`(?m)rule\s+(\d+)\s+\{((?:.|\n)*?)\n\}`)
    var str = `rule 101 {
  action allow
  source 192.168.1.0/24
  destination 10.0.0.0/8
}
rule 202 {
  action deny
  source 10.0.0.0/8
  destination 192.168.1.0/24
  description Block Internal Traffic
}`
    
    output := re.FindAllString(str, -1)
    fmt.Println(output)
}
