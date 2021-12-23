package main

import (
	"flag"
	"fmt"
//	"io/ioutil"
//	"strconv"
//	"strings"
//	"math"
	"github.com/montanaflynn/stats"
)

var inputFile = flag.String("inputFile", "inputs/day05.input", "Relative file path to use as input.")

func main() {
	nums := []float64{16,1,2,0,4,2,7,1,2,14}	
	//o, _ := stats.QuartileOutliers(nums)
	max, _ := stats.Max(nums)
	min, _ := stats.Min(nums)	

	fmt.Println(max, min)
	// Output:  {Mild:[15 18] Extreme:[-1000 100]}
}
