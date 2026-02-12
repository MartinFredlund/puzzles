package main

func main() {

	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 2
	result := search(nums, target)
	println(result)
}

func search(nums []int, target int) int {
	minSpan := 0
	maxSpan := len(nums) - 1
	for minSpan <= maxSpan {
		i := minSpan + (maxSpan-minSpan)/2
		if nums[i] == target {
			return i
		} else if nums[i] > target {
			maxSpan = i - 1
		} else {
			minSpan = i + 1
		}
	}
	return -1

}