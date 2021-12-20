package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
//	"math"
)

var inputFile = flag.String("inputFile", "inputs/day05.input", "Relative file path to use as input.")

type Point struct {
	x int
	y int
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
	var grid map[Point]int
	grid = make(map[Point]int)

	for _, line := range split {
		s := strings.Split(line, " -> ")
		str := strings.Split(s[0], ",")
		x1, _ := strconv.Atoi(str[0])
		y1, _ := strconv.Atoi(str[1])
		start := Point{ x : x1, y : y1 }

		str = strings.Split(s[1], ",")		
		x2, _ := strconv.Atoi(str[0])
		y2, _ := strconv.Atoi(str[1])
		end := Point{ x : x2, y : y2 }		

		// Horizontal
		if (start.y == end.y) {
			if (start.x < end.x) {
				x1 = start.x
				x2 = end.x
			} else {
				x1 = end.x
				x2 = start.x			
			}

			for x := x1; x <= x2; x++ {
				p := Point{ x : x, y : start.y }
				grid[p] = grid[p] + 1
			}

		// Vertical			
		} else if (start.x == end.x)  { 
			if (start.y < end.y) {
				y1 = start.y
				y2 = end.y
			} else {
				y1 = end.y
				y2 = start.y			
			}
			
			for y := y1; y <= y2; y++ {
				p := Point{ y : y, x : start.x }
				grid[p] = grid[p] + 1
			}
		}
		// Diagonal
	}

	// Part 1
	ans := 0
	for _,v := range grid {
		if v >= 2 {
			ans++
		}
	}
	fmt.Println("Part 1: ", ans)
}
