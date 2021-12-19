package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day03.input", "Relative file path to use as input.")

type bit struct {
	position int
	count int
}


// Based on length of binary string
func getHighestBit(length int) int {
	s := string("1" + strings.Repeat("0", length-1))
	hb, _ := strconv.ParseInt(s, 2, 0)
	return int(hb)
}

func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n")

	// Part 1
	var bit map[int]int   //map[position] = count of 1s
	bit = make(map[int]int)
	highestBit := getHighestBit(len(split[0]))
	
	for _, binary := range split {
		i,_ := strconv.ParseInt(binary, 2, 0)

		for pos := highestBit; pos >= 1; pos = pos / 2 {
			if (int(i) & pos) > 0 {
				bit[pos]++ 	// Count the number of "1's" found in each bit
			}
		}
	}

	var gamma int = 0
	var epsilon int = 0	
	for pos, cnt := range bit {
		// If most common bit is "1", set bit at this pos in final number
		if cnt > len(split)/2 {
			gamma = gamma | pos			
		} else {
			epsilon = epsilon | pos						
		}
	}

	fmt.Println("Part1: g,e,ans", gamma, epsilon, gamma*epsilon)

	fmt.Printf("Part 1 binary: %b, %b\n", gamma, epsilon)

	// Part 2
	var set map[int]bool
	set = make(map[int]bool)
	for pos := highestBit; pos >= 1; pos = pos / 2 {
		mostCommon := 0
		leastCommon := 0
		
		fmt.Println(">>>>", pos)
		for _, binary := range split {
			i,_ := strconv.ParseInt(binary, 2, 0)
			if pos == highestBit || set[int(i)] == true {
				if (pos & gamma) == (pos & int(i)) {
					set[int(i)] = true
					mostCommon++
				} else {
					set[int(i)] = false
					leastCommon++
				}
			}
		}

		// Purge set of unwanted
		for k, _ := range set {
			if (mostCommon == leastCommon) { // special case - counts equal favor "1"
				if (k & pos > 0) { 
					fmt.Println("A", k, pos, k & pos)
					set[k] = true
				} else {
					set[k] = false
				}
			}
			
			if set[k] == false {
				fmt.Println("B", k, pos, k & pos, set[k])
			//	delete(set, k)
			}
		}

		for k := range set {
			if (set[k] == true) {
				fmt.Println("here",k, set)
			}
		}
	}
}



