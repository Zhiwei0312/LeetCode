# lambda 参数1, 参数2: 表达式

# try:
#     # 可能出错的代码
# except ExceptionType:
#     # 出错时执行
# else:
#     # 没出错才执行（可选）
# finally:
#     # 无论如何都会执行
from operator import add, sub, mul

# 按从左到右顺序执行
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        N = len(tokens)
        stack = []
        operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x,y: int(x/y)
        }

        for i in range(N):
            tok = tokens[i]

            try:
                num = int(tok)
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                num = operations[tok](num1,num2)
            finally:
                stack.append(num)
        return stack[-1]