class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        temp = ""
        for char in s:
            pos = temp.find(char)
            if pos == -1:
                temp += char
            else:
                answer = max(answer, len(temp))
                temp = temp[pos + 1 :] + char
        answer = max(answer, len(temp))
        return answer
