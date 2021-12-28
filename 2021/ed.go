package main

import (
	"fmt"
	"github.com/deckarep/golang-set"
)

type SignalToSegmentMap map[string]string
type SegmentToValueMap map[string]int
type BinaryToDisplayMap map[int]int

var SegmentValue SegmentToValueMap
var DisplayMap BinaryToDisplayMap

var one, four, seven, eight mapset.Set // well known displays

func main() {
	var signal [10]mapset.Set

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


	
	wires := Analysis(signal)
	output := [4]string {"cdfeb", "fcadb", "cdfeb", "cdbaf"}

	InitDisplayMap()
	RenderOutput( wires, output )
}

func Analysis(signal [10]mapset.Set) SignalToSegmentMap {
	found := mapset.NewSet()
	segmentMap := make(SignalToSegmentMap) 
	
	set := seven.Difference(one)
	AddFoundSegment( set, "a", segmentMap, found)

	// Five cardinality 
	for _, sig := range signal {
		if sig.Cardinality() == 5 { // 2, 3 or 5
			if (sig.Intersect(one).Equal(one)) { // THREE
				three := sig

				set = four.Difference(three)
				AddFoundSegment( set, "b", segmentMap, found)				
				
				set = three.Difference(seven).Difference(four)
				AddFoundSegment( set, "g", segmentMap, found)				

				set = three.Difference(seven).Difference( mapset.NewSetFromSlice ([]interface{}{segmentMap["g"]}))
				AddFoundSegment( set, "d", segmentMap, found)
			}
		}
	}

	// Six cardinality 
	for _, sig := range signal {
		if sig.Cardinality() == 6 { // 6, 9 or 0
			set = one.Difference(sig)
			if set.Cardinality() == 1 { // FOUND SIX
				six := sig
				AddFoundSegment( set, "c", segmentMap, found)

				set = six.Difference(found).Difference(one)
				AddFoundSegment( set, "e", segmentMap, found)				

				set = eight.Difference(found)
				AddFoundSegment( set, "f", segmentMap, found)								
			}
		}
	}
				
	return segmentMap
}

func RenderOutput( segmentMap SignalToSegmentMap, output [4]string) {
	
	for _, o := range output {
		segsBinary := 0
		for _, s := range o {
			letter := string(s)
			segsBinary |= SegmentValue [ segmentMap[letter] ]
//			fmt.Println(letter, segmentMap[letter], SegmentValue [ segmentMap[letter] ])
		}

		fmt.Println(">> ",o, segsBinary, DisplayMap[ segsBinary ])
	}
}


func AddFoundSegment(signalLetter mapset.Set, wireLetter string, segmentMap SignalToSegmentMap, found mapset.Set) {
	s := signalLetter.Pop().(string)
	segmentMap[s] = wireLetter
	found.Add(s)
}

func InitDisplayMap() {
	// based on https://en.wikipedia.org/wiki/Seven-segment_display#cite_ref-TI_1974_SR-22_23-1	- remapped from std for this puzzle
	//   abcdefg
	// 01111111 = "8"
	SegmentValue = make(SegmentToValueMap)
	SegmentValue["a"] = 64
	SegmentValue["b"] = 2	
	SegmentValue["c"] = 32
	SegmentValue["d"] = 1
	SegmentValue["e"] = 4	
	SegmentValue["f"] = 16
	SegmentValue["g"] = 8

	DisplayMap = make(BinaryToDisplayMap)
	
	DisplayMap[0x7E] = 0
	DisplayMap[0x30] = 1
	DisplayMap[0x6D] = 2
	DisplayMap[0x79] = 3
	DisplayMap[0x33] = 4
	DisplayMap[0x5B] = 5
	DisplayMap[0x5F] = 6
	DisplayMap[0x70] = 7
	DisplayMap[0x7F] = 8
	DisplayMap[0x7B] = 9

	// fmt.Println("segxToDigit", DisplayMap)
}
