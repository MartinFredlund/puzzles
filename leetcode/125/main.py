class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
    
        while True:
            if left >= right:
                return True
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
