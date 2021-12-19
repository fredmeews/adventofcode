package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day02.input", "Relative file path to use as input.")

func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n")

	var x,y int = 0,0
	// part 1
	for _, moves := range split {
		move := strings.Fields(moves)
		steps, _ := strconv.Atoi(move[1])
		
		switch move[0] {
		case "forward":
			x += steps
		case "down":
			y += steps
		case "up":
			y -= steps			
		}
	}	
	fmt.Println("Part 1: x,y,ans", x, y, x*y)
	
	// part 2
	x,y = 0,0
	var aim int = 0
	for _, moves := range split {
		move := strings.Fields(moves)
		steps, _ := strconv.Atoi(move[1])
		
		switch move[0] {
		case "forward":
			x += steps
			y += aim * steps
		case "down":
			aim += steps
		case "up":
			aim -= steps			
		}
	}	

	fmt.Println("Part 2: x,y,ans", x, y, x*y)		
}

