# 从x出发，每经过一个加油站加油，最后可以到达的加油站是y:
# sum(gas[i] from x to y-1) >= sum(cost[i] from x to y-1)
# sum(gas[i] from x to y) < sum(cost[i] from x to y)

# 考虑z加油站位于x,y之间，
# sum(gas[i] from z to y) = sum(gas[i] from x to y) - sum(gas[i] from x to z-1)
#                         < sum(cost[i] from x to y) - sum(gas[i] from x to z-1)
#                         < sum(cost[i] from x to y) - sum(cost[i] from x to z-1)
#                         = sum(cost[i] from z to y)
# 所以从x,y之间的任何一站出发都无法到达y的下一站

# 这个的解并不唯一吧...?
# cost = [3,4,4,4,4]
# gas = [3,3,4,5,6]

class Solution:
    # idea: 如果sum(gas) >= sum(cost),那一定有解
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        surplus = 0
        start = 0

        for i in range(len(gas)):
            surplus += gas[i] - cost[i]
            if surplus < 0:
                start = i + 1
                surplus = 0

        return start
    
# 用while不要用for，for会死循环
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n: # 从stop i开始
            sum_of_gas = sum_of_cost = 0
            nbStop = 0
            while nbStop < n:
                j = (i + nbStop) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_cost > sum_of_gas:
                    break
                nbStop += 1
            if nbStop == n:
                return i
            else:
                i += nbStop + 1
        return -1
    
from typing import List
import os

# wrong version with for loop
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    N = len(gas)
    startPts = 0;
    
    while startPts < N:
        surplus = 0;
        print('startPts, N-1 = ',startPts, N-1)
        for j in range(N):
            i = (j + startPts) % N;
            surplus = gas[i] - cost[i] + surplus;
            # print('i, surplus, startPts = ',i,surplus, startPts)
            if surplus < 0:
                startPts = i+1;
                if j >= N-1:
                    return -1;
                else:
                    break;
            else:
                print('i, surplus, startPts, j = ',i, surplus, startPts, j)
                if i == startPts -1:
                    return startPts

gas = [2,3,4]
cost = [3,4,3]
gas = [1,2,3,4,3,2,4,1,5,3,2,4]
cost = [1,1,1,3,2,4,3,6,7,4,3,1]

os.system('clear')
print(canCompleteCircuit(gas,cost))