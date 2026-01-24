from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        N = len(strs)
        output = []
        Count = {}

        for i in range(N):
            str1 = strs[i]
            print('str1 = ',str1)
            if str1 not in Count:
                anagram = [str1]

                for j in range(i+1,N):
                    str2 = strs[j]
                    print('str2 = ', str2)

                    if self.isAnagram(str1, str2):
                        anagram.append(str2)
                        Count[strs[j]] = Count.get(str2,0) + 1;
                        print(i,j,Count)
                output.append(anagram)

        return output

    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

    
sol = Solution()
list1 = ["eat","tea","tan","ate","nat","bat"]

Result = sol.groupAnagrams(list1)
print(Result)
print(list1)