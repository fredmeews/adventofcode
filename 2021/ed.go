package main

import (
	"fmt"
//	"io/ioutil"
//	"strconv"
//	"strings"
//	"math"
	"github.com/deckarep/golang-set"
)

func main() {
	var signal [10]mapset.Set
	//knownSegments := mapset.NewSet()
	segmentMap := make(map[string]string) // segmentMap[oldLetter] = newLetter

	var one, four, seven, eight, three, six mapset.Set
	segs := [10]string {"acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"}
	for i, str := range segs {
		signal[i] = mapset.NewSet()
		for _, c := range str {
			signal[i].Add(string(c))
		}
		switch signal[i].Cardinality() {
		case 2:
			one = signal[i]
		case 3:
			seven = signal[i]
		case 4:
			four = signal[i]
		case 7:
			eight = signal[i]
		}
	}
	fmt.Println(one, four, seven, eight)

	
	//	fmt.Printf("%T", seven.Difference(one).Pop() )

	found := mapset.NewSet()
	
	set := seven.Difference(one)
	segmentMap["a"] = set.Pop().(string)
	found.Add(segmentMap["a"])

	// Five cardinality 
	for _, sig := range signal {
		if sig.Cardinality() == 5 { // 2, 3 or 5
			if (sig.Intersect(one).Equal(one)) { // THREE
				fmt.Println("FOUND THREE:" , sig)
				three = sig

				set = four.Difference(three)
				segmentMap["b"] = set.Pop().(string)
				found.Add(segmentMap["b"])				
				
				set = three.Difference(seven).Difference(four)
				segmentMap["g"] = set.Pop().(string)
				fmt.Println(segmentMap["g"])
				found.Add(segmentMap["g"])

				set = three.Difference(seven).Difference( mapset.NewSetFromSlice ([]interface{}{segmentMap["g"]}))
				segmentMap["d"] = set.Pop().(string)
				found.Add(segmentMap["d"])

				set = eight.Difference(found)
				segmentMap["f"] = set.Pop().(string)
				found.Add(segmentMap["f"])
			}
		}
	}

	// Six cardinality 
	for _, sig := range signal {
		if sig.Cardinality() == 6 { // 6, 9 or 0
			set = one.Difference(sig)
			if set.Cardinality() == 1 { // FOUND SIX
				six = sig
				segmentMap["c"] = set.Pop().(string)
				found.Add(segmentMap["c"])

				set = six.Difference(found).Difference(one)
				segmentMap["e"] = set.Pop().(string)
				found.Add(segmentMap["e"])

				fmt.Println(eight.Difference(found))
			}
		}
	}
				
	fmt.Println(segmentMap)
}
