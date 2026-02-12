package main

func main() {

	nums := []int{1, 3, 5, 6}
	target := 2
	result := searchInsert(nums, target)
	println(result)
}

func searchInsert(nums []int, target int) int {
	minSpan := 0
	maxSpan := len(nums) - 1
	var i = 0
	for minSpan <= maxSpan {
		i = minSpan + (maxSpan-minSpan)/2
		if nums[i] == target {
			return i
		} else if nums[i] > target {
			maxSpan = i - 1
		} else {
			minSpan = i + 1
		}
	}
	return minSpan
}