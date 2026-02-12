class Solution:
    def search(self, nums: list[int], target: int) -> int:
        minSpan = 0
        maxSpan = len(nums) - 1

        while minSpan <= maxSpan:
            mid = minSpan + int((maxSpan - minSpan) / 2)
            if nums[mid] == target:
                return mid
            if nums[minSpan] <= nums[mid]:
                if nums[minSpan] <= target <= nums[mid]:
                    maxSpan = mid - 1
                else:
                    minSpan = mid + 1
            else:
                if nums[mid] <= target <= nums[maxSpan]:
                    minSpan = mid + 1
                else:
                    maxSpan = mid - 1
        return -1


s = Solution()
print(s.search([5, 1, 3], 3))
