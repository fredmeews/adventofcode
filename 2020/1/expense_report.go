package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

	s := make([]string, 3)

func main() {
	var i int
	
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	s := bufio.NewScanner(file)
	
	for s.Scan() {
		i, err = strconv.Atoi(s.Text())
		fmt.Println(i)
	}

	if err := s.Err(); err != nil {
		log.Fatal(err)
	}
}
