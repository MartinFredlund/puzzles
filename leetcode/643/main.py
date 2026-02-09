class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_val = -float("inf")
        temp = 0
        for i in range(k):
            temp += nums[i]
        max_val = max(max_val, (temp / k))
        for n in range(k, len(nums)):
            temp -= nums[n - k]
            temp += nums[n]
            max_val = max(max_val, (temp / k))

        return max_val
