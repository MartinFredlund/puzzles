class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = len(nums) - 1
        f = 0
        result = [0 for _ in range(len(nums))]
        r = l
        for _ in range(len(nums)):
            if abs(nums[f]) > abs(nums[l]):
                temp = nums[f] ** 2
                f += 1
            else:
                temp = nums[l] ** 2
                l -= 1
            result[r] = temp
            r -= 1
        return result
