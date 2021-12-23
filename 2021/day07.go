package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day07.input", "Relative file path to use as input.")

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
	crabs := make(map[int]int)
	for _, v := range split {
		i,_ := strconv.Atoi(v)
		crabs[i]++
	}

	// get max & min
	max := -1
	min := 1000000
	for k,_ := range crabs {
		if k > max {
			max = k
		} else if k < min {
			min = k
		}
	}

	// loop through from min to max to find the least fuel
	leastFuel := 1000000
	for pos := min; pos <= max; pos++ {
		distance, fuel := 0,0
		for k,v := range crabs {
			distance = pos - k
			if (distance < 0) {
				distance = -distance // abs
			}
			fuel += distance * v
		}
		if fuel < leastFuel {
			leastFuel = fuel
		}
	}

	fmt.Println(leastFuel)
	
		
	
	// avg removing outliers
	// https://www.thoughtco.com/what-is-an-outlier-3126227
//	fmt.Println(crabs, (sum-14-16)/8, len(split))
}
