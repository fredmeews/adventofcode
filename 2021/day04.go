package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	//	"unicode/utf8"
//	"gonum.org/v1/gonum/mat"
)

var inputFile = flag.String("inputFile", "inputs/day04.input", "Relative file path to use as input.")

	
type Cell struct {
	num int64
	marked bool
}

type Card [5][5]Cell


func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n\n")

	fmt.Println(moves)

	cards := make([]Card, 0)
	for _, inputCard := range split[1:] {
		var card Card
	 	for ir, row := range strings.Split(inputCard, "\n") {
	 		for ic, col := range strings.Fields(row) {
	 			num, _ := strconv.Atoi(col)
	 			card[ir][ic].num = int64(num)
	 		}
	 	}
	 	cards = append(cards, card)
	}

	// Mark winning
	moves := strings.Split(split[0], ",")
	for i, v := range moves {
		
	}
}
