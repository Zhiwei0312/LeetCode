# 对于「空字符串」以及「一个点」，我们实际上无需对它们进行处理，因为「空字符串」没有任何含义，
# 而「一个点」表示当前目录本身，我们无需切换目录。

# 对于「两个点」或者「目录名」，我们则可以用一个栈来维护路径中的每一个目录名。当我们遇到「两个点」时，
# 需要将目录切换到上一级，因此只要栈不为空，我们就弹出栈顶的目录。当我们遇到「目录名」时，就把它放入栈。

# 这样一来，我们只需要遍历 names 中的每个字符串并进行上述操作即可。在所有的操作完成后，
# 我们将从栈底到栈顶的字符串用 / 进行连接，再在最前面加上 / 表示根目录，就可以得到简化后的规范路径。

class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')

        stack = list()

        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)

        return "/" + "/".join(stack)