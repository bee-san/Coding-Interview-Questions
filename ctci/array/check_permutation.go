package main

import "testing"

func main() {
	// Two strings are permutations of eachother if they contain the same chars but in a different order
	// straight off the bat sorting them would be handy
}

func is_permutation(input1 string, input2 string) bool {
	// two strings cannot be permutations of eachother if they are of unequal size
	if len(input1) != len(input2) {
		return false
	}

	for i, rune := range input1 {

	}
	return true
}

func TestIsPermutationTrue(t *testing.T) {
	result := is_permutation(" ", " ")
	if result != true {
		t.Errorf("2 spaces are not permutations of eachother.")
	}
}

func TestIsPermutationFalse(t *testing.T) {
	result := is_permutation("a", " ")
	if result != false {
		t.Errorf("a is a permutation of space")
	}
}
