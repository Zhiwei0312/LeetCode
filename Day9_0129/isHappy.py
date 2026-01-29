# 如果它不在哈希集合中，我们应该添加它。
# 如果它在哈希集合中，这意味着我们处于一个循环中，因此应该返回 false

from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        Hash = set()
        
        totalSum = n

        while totalSum not in Hash and totalSum != 1:
            Hash.add(totalSum)
            totalSum = self.getSum(totalSum)
        
        if totalSum == 1:
            return True
        else:
            return False

        


    def getSum(self, n:int) -> int:
        output = 0

        while n >0:
            n,digit = divmod(n,10)
            output += digit ** 2
        
        return output
    
# 那么这个问题就可以转换为检测一个链表是否有环。因此我们在这里可以使用弗洛伊德循环查找算法。
# 这个算法是两个奔跑选手，一个跑的快，一个跑得慢。在龟兔赛跑的寓言中，跑的慢的称为 “乌龟”，跑得快的称为 “兔子”。

# 不管乌龟和兔子在循环中从哪里开始，它们最终都会相遇。这是因为兔子每走一步就向乌龟靠近一个节点（在它们的移动方向上）。

# 我们不是只跟踪链表中的一个值，而是跟踪两个值，称为快跑者和慢跑者。在算法的每一步中，慢速在链表中前进 1 个节点，快跑者前进 2 个节点（对 getNext(n) 函数的嵌套调用）。

# 如果 n 是一个快乐数，即没有循环，那么快跑者最终会比慢跑者先到达数字 1。

# 如果 n 不是一个快乐的数字，那么最终快跑者和慢跑者将在同一个数字上相遇。

    def isHappy_linkedList(self,n:int) -> bool:
        slow_runner = n
        fast_runner = self.getSum(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = self.getSum(slow_runner)
            fast_runner = self.getSum(self.getSum(fast_runner))
        return fast_runner == 1
