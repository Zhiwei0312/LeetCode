from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        N = len(intervals)

        flag = 0
        for i in range(N):
            if intervals[i][0] < newInterval[0]:
                output.append(intervals[i])
            else:
                if flag == 0:
                    output.append(newInterval);flag = 1
                    output.append(intervals[i])
                else:
                    output.append(intervals[i])
        if flag == 0:
            output.append(newInterval)
        print(output)

        merged = [];
        for i in range(N+1):
            interval = output[i]
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1],interval[1])

        print(merged)
        return merged
    
sol = Solution()
intervals = [[1,5]]
newInterval = [2,3]

print(sol.insert(intervals,newInterval))