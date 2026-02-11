class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        foundNums = {}
        for i, n in enumerate(nums):
            if n in foundNums:
                if abs(foundNums[n] - i) <= k:
                    return True
            foundNums[n] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
