package main

import (
	"flag"
	"fmt"
	"io/ioutil"
//	"strconv"
	"strings"
	"os"
	"sort"
)

// display[segment bits on] = digit
type BitsToNumberDisplayed map[int]int
type SegmentToBitmask map[string]int


var segsToDigit BitsToNumberDisplayed 

type Wires struct {
	signals []string
	output []string
}


func main() {
	InitDisplayMap()
	split := strings.Split(ReadFile(), "\n")
	wires := make([]Wires, len(split))

//	part1Count := 0
	for ix, line := range split {
		s := strings.Split(line, " | ")
		
		wires[ix].signals = strings.Split(s[0], " ")
		wires[ix].output = strings.Split(s[1], " ")

		for _,s := range wires[ix].signals {
			fmt.Println("wire: ", SortString(string(s)))
		}
		for _,s := range wires[ix].output {
			fmt.Println("segm: ", SortString(string(s)))
		}		
	}

	// Figure out new mapping of signal to segment
	//
	// - Given 1, 4, 7 - you can figure out "a" segment
	// 

	PartTwo()
}

func SortString(w string) string {
    s := strings.Split(w, "")
    sort.Strings(s)
    return strings.Join(s, "")
}

func InitDisplayMap() {
	// based on https://en.wikipedia.org/wiki/Seven-segment_display#cite_ref-TI_1974_SR-22_23-1	
	//   abcdefg
	// 01111111 = "8"
	OriginalMapping = make(SegmentToBitmask)
	OriginalMapping["a"] = 64
	OriginalMapping["b"] = 2	
	OriginalMapping["c"] = 32
	OriginalMapping["d"] = 1
	OriginalMapping["e"] = 4	
	OriginalMapping["f"] = 16
	OriginalMapping["g"] = 8

	NumberDisplayed = make(BitsToNumberDisplayed)
	
	NumberDisplayed[0b01111110] = 0
	NumberDisplayed[0b00110000] = 1
	NumberDisplayed[0b01101101] = 2
	NumberDisplayed[0b01111001] = 3
	NumberDisplayed[0b00110011] = 4
	NumberDisplayed[0b01011011] = 5
	NumberDisplayed[0b01011111] = 6
	NumberDisplayed[0b01110000] = 7
	NumberDisplayed[0b01111111] = 8
	NumberDisplayed[0b01111011] = 9

	fmt.Println("segxToDigit", NumberDisplayed)
}

func PartTwo() {
	// This puzzle map is different than typical 7-seg display
	i := Render(mapping, "cf")
	fmt.Println(i)
}

func Render(mapping map[string]int, segment string) int {
	segs := 0
	for _, c := range segment {
		s := string(c)
		segs |= mapping[s]
	}
	
	return segmentsToDisplay[segs]
}


func ReadFile() string {
	args := os.Args
	ext := "input"
	if len(args) > 1 {
		ext = "sample"
	}
	fileName := "inputs/" + args[0][strings.LastIndex(args[0], "/")+1:] + "." + ext
	var inputFile = flag.String("inputFile", fileName, "Relative file path to use as input.")
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
	 	fmt.Println(err)	
		os.Exit(-1)
	}
	return string(bytes)
}
