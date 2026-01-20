from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Nouter = len(strs)

        if Nouter == 0:
            return ""
        elif Nouter == 1:
            return len(strs[0])

        N1 = len(strs[0])
        str1 = strs[0]
        for i in range(1,Nouter-1):
            str2 = strs[i]

            N2 = len(str2)
            N = min(N1, N2)
            print("N1, N2, N = ", N1, N2, N)

            strNew = ""
            for j in range(N):
                if str1[j] == str2[j]:
                    strNew += str1[j]
                else:
                    break;
            
            N1 = len(strNew)
            str1 = strNew

        return str1
    
sol = Solution()

strings = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strings))
                