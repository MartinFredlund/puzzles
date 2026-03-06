class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            odd = expand(s,i,i)
            even = expand(s,i,i+1)
            longest = odd if len(odd)>len(longest) else longest
            longest = even if len(even)>len(longest) else longest
        return longest

def expand(s,left, right):
    while left >= 0 and right < len(s) and s[left]==s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

s = Solution()
print(s.longestPalindrome("babad"))
