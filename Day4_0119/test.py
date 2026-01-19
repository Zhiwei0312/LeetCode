from typing import List
import os

class Solution:
# 两次遍历
# 左规则：当 ratings[i−1]<ratings[i] 时，i 号学生的糖果数量将比 i−1 号孩子的糖果数量多。
# 右规则：当 ratings[i]>ratings[i+1] 时，i 号学生的糖果数量将比 i+1 号孩子的糖果数量多。

# 我们遍历该数组两次，处理出每一个学生分别满足左规则或右规则时，最少需要被分得的糖果数量。
# 每个人最终分得的糖果数量即为这两个数量的最大值。
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        nb = [1] * N;


        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                nb[i] = nb[i-1] + 1;
        
        for i in reversed(range(N-1)):
            if ratings[i] > ratings[i+1]:
                nb[i] = max(nb[i+1] + 1,nb[i]);
            

        print(nb)
        return sum(nb)        

os.system('clear')
sol = Solution()
# result = sol.candy([1,0,2])
# result = sol.candy([1,2,2])
result = sol.candy([1,2,87,87,87,2,1])
print(result)

# def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
#     N = len(gas)
#     startPts = 0;
    
#     while startPts < N:
#         surplus = 0;
#         print('startPts, N-1 = ',startPts, N-1)
#         for j in range(N):
#             i = (j + startPts) % N;
#             surplus = gas[i] - cost[i] + surplus;
#             # print('i, surplus, startPts = ',i,surplus, startPts)
#             if surplus < 0:
#                 startPts = i+1;
#                 if j >= N-1:
#                     return -1;
#                 else:
#                     break;
#             else:
#                 print('i, surplus, startPts, j = ',i, surplus, startPts, j)
#                 if i == startPts -1:
#                     return startPts

# gas = [2,3,4]
# cost = [3,4,3]
# gas = [1,2,3,4,3,2,4,1,5,3,2,4]
# cost = [1,1,1,3,2,4,3,6,7,4,3,1]

# os.system('clear')
# print(canCompleteCircuit(gas,cost))