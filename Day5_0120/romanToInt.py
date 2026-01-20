from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        val = {}
        val['I'] = 1
        val['V'] = 5
        val['X'] = 10
        val['L'] = 50
        val['C'] = 100
        val['D'] = 500
        val['M'] = 1000
        val['IV'] = 4
        val['IX'] = 9
        val['XL'] = 40
        val['XC'] = 90
        val['CD'] = 400
        val['CM'] = 900

        N = len(s)
        if N == 0:
            return 0
        elif N == 1:
            return val[s]

        i = 0;
        answer = 0;

        while i <= N-1:
            print(i, answer)
            if val[s[i]] >= val[s[min(N-1,i+1)]]:
                answer += val[s[i]]
                i += 1
            else:

                answer += val[s[i:i+2]]
                i += 2
        return answer
    
sol = Solution()
print(sol.romanToInt('MCMXCIV'))

