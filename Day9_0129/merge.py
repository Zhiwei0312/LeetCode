from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)

        # 按左端点排序
        intervals.sort(key = lambda x: x[0])

        output = [];
        for i in range(N):
            interval = intervals[i]
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not output or interval[0] > output[-1][1]:
                output.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                output[-1][1] = max(output[-1][1],interval[1])
        return output


sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
sol.merge(intervals)