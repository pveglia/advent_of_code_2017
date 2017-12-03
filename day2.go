package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func loadFile() [][]int64 {
	var res [][]int64
	bytes, err := ioutil.ReadFile("day2.input.txt")
	if err != nil {
		log.Println("could not read file")
	}
	stringLines := strings.Split(string(bytes), "\n")
	for _, stringLine := range stringLines {
		var line []int64
		fields := strings.Split(stringLine, "\t")
		for _, fieldStr := range fields {
			field, _ := strconv.ParseInt(fieldStr, 10, 64)
			line = append(line, field)
		}
		res = append(res, line)
	}
	return res
}

func part1() {
	bytes, err := ioutil.ReadFile("day2.input.txt")
	if err != nil {
		log.Println("could not read file")
	}
	lines := strings.Split(string(bytes), "\n")
	var sum int64
	for _, line := range lines {
		// fmt.Println("line", line)
		fields := strings.Split(line, "\t")
		var min, max int64
		for idx, fieldStr := range fields {
			field, _ := strconv.ParseInt(fieldStr, 10, 64)
			if idx == 0 {
				min = field
				max = field
				continue
			}
			if field < min {
				min = field
			}
			if field > max {
				max = field
			}
		}
		diff := max - min
		sum += diff
	}
	fmt.Println(sum)
}

func part2() {
	matrix := loadFile()
	var sum int64
	for lineIdx, line := range matrix {
		fmt.Println("line", lineIdx)
	lineLoop:
		for i := 0; i < len(line)-1; i++ {
			for j := i + 1; j < len(line); j++ {
				var a, b int64
				if line[i] > line[j] {
					a = line[i]
					b = line[j]
				} else {
					a = line[j]
					b = line[i]
				}
				fmt.Println(i, j, a, b, a%b)
				if a%b == 0 {
					fmt.Println("found on line", lineIdx, a, b)
					sum += a / b
					break lineLoop
				}
			}
		}
	}
	fmt.Println(sum)
}

func main() {
	part2()
}
