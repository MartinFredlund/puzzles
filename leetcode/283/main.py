class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow_pointer], nums[i] = nums[i], nums[slow_pointer]
                slow_pointer += 1
        print(nums)

s = Solution()
s.moveZeroes(nums=[0,1,0,3,12])

