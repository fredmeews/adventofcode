package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"gonum.org/v1/gonum/mat"
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
//	moves := strings.Split(split[0], ",")
	
//	fmt.Println(moves)

	data := make([]float64, 25)	
	for _, inputCard := range split[1:] {
		for i, n := range strings.Fields(inputCard) {
			data[i], _ = strconv.ParseFloat(n, 64)
		}
		m :=  mat.NewDense(5, 5, data)
//		matPrint(m)

		//matPrint(m.ColView(4))
		v := m.ColView(4)
		for i := 0; i < v.Len(); i++ {
			fmt.Println("vec = ", v.AtVec(i))
		}
		fmt.Println("--------")

		v = m.RowView(4)
		for i := 0; i < v.Len(); i++ {
			fmt.Println("vec = ", v.AtVec(i))
		}
		fmt.Println("--------")		

		d := m.DiagView()
		matPrint(d)
	}

}

func matPrint(X mat.Matrix) {
	fa := mat.Formatted(X, mat.Prefix(""), mat.Squeeze())
	fmt.Printf("%v\n", fa)
}
