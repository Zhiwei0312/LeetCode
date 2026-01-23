from typing import List
# what is KMP?

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(haystack), len(needle)

        if N == M:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(N - M  + 1):
            print("N, M, i = ", N, M, i)
            idx = 0;
            j = i;
            while idx < M and haystack[j] == needle[idx]:
                print(haystack[i], needle[idx])
                j += 1
                idx += 1
            if idx == M:
                print(idx,M,i-M)
                return i - M

        return -1

    def strStr_KMP(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        # 1) build lps
        lps = [0] * m
        j = 0  # length of current matched prefix in needle
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j

        # 2) match
        j = 0  # how many chars matched in needle
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
                if j == m:
                    return i - m + 1

        return -1


    
sol = Solution()

haystack = "ABABDABCD"
needle = "ABAB"
sol.strStr(haystack,needle)
