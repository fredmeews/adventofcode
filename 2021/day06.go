package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day06.input", "Relative file path to use as input.")

const DAYS=80
const RESET_TIMER=6
const BABY=8


func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, ",")

	fish := make([]int, len(split))
	for ix, v := range split {
		fish[ix], _ = strconv.Atoi(v)
	}

	// Part 1
	for i := 0; i < DAYS; i++ {
		fish = tick(fish)
		fmt.Printf("Day %v:  %v\n", i, fish)
	}
}

func tick(fish []int) []int {
	size := len(fish)
	for i := 0; i < size; i++ {
		fish[i]--
		if fish[i] < 0 {
			fish[i] = RESET_TIMER
			fish = append(fish, BABY)
		}
	}
	return fish
}
