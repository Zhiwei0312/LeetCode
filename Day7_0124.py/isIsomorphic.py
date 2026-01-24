from typing import List

class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        f = {}
        for i,st in enumerate(s):
            print(i,st)

        return True
    
sol = Solution()
s = 'egg'
t = 'add'

result = sol.isIsomorphic(s,t)
print(result)