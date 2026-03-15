class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        result = list(s)
        vowels = set("aeiouAEIOU")
        while left < right:
            if result[left] not in vowels:
                left += 1
            elif result[right] not in vowels:
                right -= 1
            else:
                result[right], result[left] = result[left], result[right]
                left += 1
                right -= 1
        return "".join(result)


s = Solution()
print(s.reverseVowels("IceCreAm"))
