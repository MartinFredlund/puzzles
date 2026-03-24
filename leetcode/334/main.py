from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s1, s2 = float("inf"), float("inf")
        for num in nums:
            if num <= s1:
                s1 = num
            elif num <= s2:
                s2 = num
            else:
                return True
        return False


S = Solution()
print(S.increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))
