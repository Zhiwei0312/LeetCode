# 设 numRows 行字符串分别为 s1, s2, … , sn ，则容易发现：按顺序遍历字符串 s 时，
# 每个字符 c 在 N 字形中对应的 行索引 先从 s1增大至 sn ，再从 sn减小至 s1 …… 如此反复。
# 因此解决方案为：模拟这个行索引的变化，在遍历 s 中把每个字符填到正确的行 res[i] 

# res[i] += c： 把每个字符 c 填入对应行 si ；
# i += flag： 更新当前字符 c 对应的行索引；
# flag = - flag： 在达到 Z 字形转折点时，执行反向

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        res = ["" for _ in range(numRows)]

        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows -1:
                flag = - flag
            
            i += flag

        return "".join(res)
