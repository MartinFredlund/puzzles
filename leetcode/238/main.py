import operator
from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = reduce(operator.mul, nums[:i] + nums[i + 1 :], 1)
        return result


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [
            reduce(operator.mul, nums[:i] + nums[i + 1 :], 1) for i in range(len(nums))
        ]


class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        temp = 1
        for i in range(len(nums)):
            result[i] += temp
            temp *= nums[i]
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]
        return result


s = Solution3()
print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
