from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip()
        s = s.rstrip()

        N = len(s)
        answer = []
        flag = 0;
        ss = ""
        for i in reversed(range(N)):
            if flag == 0 and s[i] == " ":
                flag = 1;
                answer.append(ss)
                ss = ""
            elif i == 0:
                ss = s[i] + ss
                answer.append(ss)
            else:
                flag = 0;
                ss = s[i] + ss
        print(answer)
        return " ".join(answer)
    
sol = Solution()
strings = "a good   example"

print(sol.reverseWords(strings))