from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')

        fwd = {}
        for i,pa in enumerate(pattern):
            if pa not in fwd:
                fwd[pa] = s[i]
            else:
                if fwd[pa] != s[i]:
                    return False
                
        bwd = {}
        for i,pa in enumerate(s):
            if pa not in bwd:
                bwd[pa] = pattern[i]
            else:
                if bwd[pa] != pattern[i]:
                    return False
        return True
    
sol = Solution()
pattern = "abba"
s = "dog cat cat dog"
result = sol.wordPattern(pattern,s)