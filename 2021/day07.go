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
	leastFuel, leastFuel2 := 1000000, 1000000188
	for pos := min; pos <= max; pos++ {
		distance, distance2, fuel, fuel2 := 0,0,0,0
		for k,v := range crabs {
			distance = pos - k
			if (distance < 0) {
				distance = -distance // abs
			}
			distance2 = part2(distance)
//			fmt.Println(pos, distance, distance2)
			
			fuel += distance * v
			fuel2 += distance2 * v			
		}
		if fuel < leastFuel {
			leastFuel = fuel
		}
		if fuel2 < leastFuel2 {
			leastFuel2 = fuel2
		}
	}

	fmt.Println(leastFuel, leastFuel2)
}

func part2(distance int) int {
	d2 := 0
	for i := 1; i <= distance; i++ {
		d2 += i
	}
	return d2
}
