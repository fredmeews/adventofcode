package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day01.input", "Relative file path to use as input.")

func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n")

	//part 1
	increases := 0
	for j := 1; j < len(split);  j++ {
		a,_ := strconv.Atoi(split[j])		
		b,_ := strconv.Atoi(split[j-1])

		if a > b {
	 		increases++
	 		fmt.Println("increase from", split[j-1], "to", split[j])
	 	}  else {
			 fmt.Println("decrease from", split[j-1], "to", split[j])
		 }
	}
	fmt.Println("len:", len(split), "increases", increases)
	
	// part 2
	increases = 0
	var sums []int

	// LIZ: for this instead of re-reading the next 3-values, she used a "sliding window"
	// which every time you moved up a line, would 'remove' (subtract) the last number from the sum
	// and add the new number to it.
	for j := 2; j < len(split);  j = j+1 {
		c,_ := strconv.Atoi(split[j])		
		b,_ := strconv.Atoi(split[j-1])
		a,_ := strconv.Atoi(split[j-2])

		sums = append(sums, a+b+c)
		fmt.Println("appended", a,"+",b,"+",c)

		if (len(sums) > 1)  {
			if sums[len(sums)-1]  > sums[len(sums)-2]  {
				increases++
			}
		}

	}

	fmt.Println(sums, len(sums), increases)
}

