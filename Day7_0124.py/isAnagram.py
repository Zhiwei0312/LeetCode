from typing import List
import collections

# O(N), O(sigma)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if collections.Counter(s) - collections.Counter(t):
            return False
        
        if collections.Counter(t) - collections.Counter(s):
            return False

        return True 
    
sol = Solution()
s = 'anagram'
t = 'nagaram'
sol.isAnagram(s,t)
