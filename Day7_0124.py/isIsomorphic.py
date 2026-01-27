# 双向hash table

from typing import List
class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        f = {}
        for i,st in enumerate(s):
            if st not in f:
                f[st] = t[i]
            else:
                if f[st] != t[i]:
                    return False
                
        f = {}
        for i,st in enumerate(t):
            if st not in f:
                f[st] = s[i]
            else:
                if f[st] != s[i]:
                    return False
                
        return True
                
        

    
sol = Solution()
s = 'egg'
t = 'add'

result = sol.isIsomorphic(s,t)
print(result)