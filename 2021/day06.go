package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day06.input", "Relative file path to use as input.")

const DAYS=256
const RESET=6
const BABY=8

type Fish struct {
	yesterday int
	today int
}

func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, ",")

	// Set Initial state
	var fish [9]Fish
	for _, v := range split {
		ix,_ := strconv.Atoi(v)
		fish[ix].today++
	}

	// Cycle through days
//	fmt.Println("          0     1     2     3     4     5     6     7     8")
//	fmt.Printf("Initial %v\n", fish)	
	for i := 1; i <= DAYS; i++ {
		fish = tick(fish)
//		fmt.Printf("Day %v:  %v\n", i, fish)
	}

	// Sum total fish
	sum := 0
	for i := 0; i <= 8; i++ {
		sum += fish[i].today
	}
	fmt.Println("Total fish: ", sum)
}


func tick(fish [9]Fish) [9]Fish {
	for i := 0; i <= 7 ; i++ {
		fish[i].yesterday = fish[i].today // backup
	 	fish[i].today = fish[i+1].today  // e.g. 5's yesterday are 4s today
	}
	
	// reset: anything that was a zero yesterday is now a 6 ....
	fish[RESET].today += fish[0].yesterday

	// ...AND creates a baby
	fish[BABY].today = fish[0].yesterday

	return fish
}
