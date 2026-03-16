class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


s = Solution()
print(s.reverseWords("a good   example"))
