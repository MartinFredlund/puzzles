class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_val = 0
        max_val = len(nums) - 1
        while min_val <= max_val:
            mid = min_val + int((max_val - min_val) / 2)
            if nums[mid] < nums[max_val]:
                max_val = mid
            elif nums[mid] > nums[max_val]:
                min_val = mid + 1
            else:
                return nums[mid]
        return -1


s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
