## this is equal to judge whether the frequency of all letters are higher in magazine compared to ransomNote
from typing import List
import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for s in magazine:
            count[s] = count.get(s, 0) + 1

        for s in ransomNote:
            count[s] = count.get(s,0) - 1
            if count[s] < 0:
                return False

        return True
    
    def canConstruct_faster(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

print(not collections.Counter([1,2,2,3]) - collections.Counter([1,2,3,4]))

# ransomNote里还有多少字符是magazine里提供不了的部分
collections.Counter(ransomNote) - collections.Counter(magazine)