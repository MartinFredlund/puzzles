class Solution:
    def maxArea(self, height: List[int]) -> int:
       left = 0
       right = len(height)-1
       max_volume = 0

       while True:
           if left >= right:
               return max_volume
           max_volume = max (max_volume, ((right - left) * min(height[left],height[right])))
           if height[left]<=height[right]:
               left += 1
           else: 
               right -= 1

s = Solution()
print(s.maxArea([1,1]))
