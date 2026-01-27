from typing import List

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
            
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
    