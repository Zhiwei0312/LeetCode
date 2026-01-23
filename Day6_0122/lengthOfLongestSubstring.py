from typing import List

class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int:
        strings = {}

        left = 0
        maxNb = 0

        for r,ch in enumerate(s):
            print(r,ch,strings)
            if ch in strings :
                left = strings[ch] + 1
            strings[ch] = r
            maxNb = max(maxNb, r-  left + 1)

        return maxNb
    
strings = "abba"
sol = Solution()
result = sol.lengthOfLongestSubstring(strings)
print(result)