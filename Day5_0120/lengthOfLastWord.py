class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        N = len(s)
        answer = 0;

        for i in reversed(range(N)):
            if s[i] == " ":
                return answer
            else:
                answer += 1
        return answer
