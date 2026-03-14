class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [0] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
            else:
                result[i] = False
        return result


s = Solution()
print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
