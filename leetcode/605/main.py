class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        amount = 0
        bed = [0] + flowerbed + [0]
        for i in range(1, len(bed) - 1):
            if not (bed[i - 1] or bed[i] or bed[i + 1]):
                amount += 1
                bed[i] = 1
            if amount >= n:
                return True
        return False


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))
