class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      result = []
      min_len = min(len(word1), len(word2))
      for i in range(min_len):
         result.append(word1[i])
         result.append(word2[i])
      result.append(word1[min_len:])
      result.append(word2[min_len:])
      return "".join(result)

s = Solution()
print(s.mergeAlternately(word1 = "ab", word2 = "pqrs"))
