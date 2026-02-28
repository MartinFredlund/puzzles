from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        max_size = 0
        zero_allowance = k

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_allowance -= 1

            while zero_allowance < 0:
                if nums[left] == 0:
                    zero_allowance += 1
                left += 1

            max_size = max(max_size, i - left + 1)

        return max_size


s = Solution()
print(s.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
