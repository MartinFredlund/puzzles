package main

import "fmt"

func main(){
	var name string
	var years int

	fmt.Scan(&name)
	fmt.Scan(&years)

	for i:=0; i< years; i++ {
		fmt.Printf("Hipp hipp hurra, %s!\n", name)
	}
}