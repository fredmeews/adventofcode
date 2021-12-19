package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
//	"unicode/utf8"
)

var inputFile = flag.String("inputFile", "inputs/day03.input", "Relative file path to use as input.")

type bit struct {
	position int
	count int
}


// Based on length of binary string
func getHighestBit(length int) int64 {
	s := string("1" + strings.Repeat("0", length-1))
	hb, _ := strconv.ParseInt(s, 2, 0)
	return hb
}

func initializeSet(contents []string) map[int64]bool {
	var set map[int64]bool
	set = make(map[int64]bool)
	
	for _, binary := range contents {
		i,_ := strconv.ParseInt(binary, 2, 0)
		set[i] = true
	}
	return set
}

func printSet(set map[int64]bool) {
	for k, v := range set {
		if v == true {
			fmt.Printf("%05b, %v",k, k )
		}
	}
	fmt.Printf("\n")
	return;
}

func getFilteredSet(set map[int64]bool, pos int64, leastCommon bool) map[int64]bool {
	// Figure out most common in set
	zerosMostCommon := false
	zeros := 0
	ones := 0
	for k, v := range set {
		if v == true { 
			if (k & pos > 0) {
				ones++
			} else {
				zeros++
			}
		}
	}
	if (zeros > ones) {
		zerosMostCommon = true
	}

	// Filter set based on common
	for k, v := range set {
		if v == true {
			if (k & pos == 0) {
				set[k] = (zerosMostCommon == true)
			} else {
				set[k] = (zerosMostCommon == false)
			}
			if (leastCommon == true) {
				set[k] = !set[k]
			}
		}
		if set[k] == false {
			delete(set, k)
		}
	}

	return set
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
	highestBit := getHighestBit(len(split[0]))	

	set := initializeSet(split)
	for pos := highestBit; (pos >= 1 && len(set) > 1); pos = pos / 2 {
		set = getFilteredSet(set, pos, false)
	}
	fmt.Println ("\n>> Most common = ")
	printSet(set)

	set = initializeSet(split)
	for pos := highestBit; (pos >= 1 && len(set) > 1); pos = pos / 2 {
		set = getFilteredSet(set, pos, true)
	}
	fmt.Println ("\n>> Least common = ")
	printSet(set)
}
