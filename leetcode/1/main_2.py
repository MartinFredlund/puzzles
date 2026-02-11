class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        foundNums = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in foundNums:
                return [foundNums.get(temp), i]
            foundNums[n] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
