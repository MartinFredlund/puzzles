class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            ans = target - nums[a]
            for b in range(a + 1, len(nums)):
                if nums[b] == ans:
                    return [a, b]
