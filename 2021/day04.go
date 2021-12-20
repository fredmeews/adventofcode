package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

var inputFile = flag.String("inputFile", "inputs/day04.input", "Relative file path to use as input.")

	
type Card struct {
	cell [5][5]int
	sumUnmarked int
	won bool

	rowWin[5] int
	colWin[5] int
}
	


func main() {
	flag.Parse()
	bytes, err := ioutil.ReadFile(*inputFile)
	if err != nil {
		fmt.Println(err)	
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n\n")

	moves := strings.Split(split[0], ",")
//	fmt.Println(moves)

	// Read cards into struct
	cards := make([]Card, 0)
	for _, inputCard := range split[1:] {
		var c Card
	 	for ir, row := range strings.Split(inputCard, "\n") {
	 		for ic, col := range strings.Fields(row) {
	 			num, _ := strconv.Atoi(col)
	 			c.cell[ir][ic] = num
				c.sumUnmarked += num
	 		}
	 	}
	 	cards = append(cards, c)
	}
	//	fmt.Println(cards)

	for _, m := range moves {
		num, _ := strconv.Atoi(m)
		for idx, _ := range cards {
			if (cards[idx].won) {
				continue
			}
				
			x, y, found := findNum(num, cards[idx])
			if (found) {
//				fmt.Println("num", num, "cd", idx, "found at: ", x,y)
				cards[idx].sumUnmarked -= num
				cards[idx].colWin[x] ++
				cards[idx].rowWin[y]++

				if (isWinner(cards[idx], x, y)) {
					cards[idx].won = true
					fmt.Printf("Part 1: %v * %v = %v\n", cards[idx].sumUnmarked,
						num, cards[idx].sumUnmarked*num)
				}
			}
		}
	}
}

func findNum(num int, cd Card) (int, int, bool) {
	for ir, row := range cd.cell {
		for ic, v := range row {
			if (num == v) {
				return ic, ir, true
			}
		}
	}
	return -1, -1, false
}
	
func isWinner(cd Card, x int, y int) bool {
//	fmt.Printf("col %v = %v, row %v = %v\n\n", x, cd.colWin[x], y, cd.rowWin[y])
	return (cd.colWin[x] == 5) || (cd.rowWin[y] == 5)
}
