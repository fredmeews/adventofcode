package main

import (
	"flag"
	"fmt"
	"io/ioutil"
//	"strconv"
	"strings"
	"os"
)

type Display struct {
	signals []string
	output []string
}


func main() {
	split := strings.Split(ReadFile(), "\n")
	display := make([]Display, len(split))

	part1Count := 0
	for ix, line := range split {
		s := strings.Split(line, " | ")
		display[ix].signals = strings.Split(s[0], " ")
		display[ix].output = strings.Split(s[1], " ")

		// https://en.wikipedia.org/wiki/Seven-segment_display#cite_ref-TI_1974_SR-22_23-1
		for _,o := range display[ix].output {
			switch len(o) {
			case 2, 4, 3, 7:
				part1Count++
			}
		}
	}
	fmt.Println("Part 1 count" , part1Count)
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

	
	
