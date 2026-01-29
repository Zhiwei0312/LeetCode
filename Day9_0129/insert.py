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

        return merged

# 当便利区间[li, ri]时：
# 1. 如果ri < left: 不重叠，在左侧
# 2. 如果li > right: 不重叠，在右侧
# 3. 重叠
    def insert_faster(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 先不加入答案，继续合并后面的
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        if not placed:
            ans.append([left, right])
        return ans

sol = Solution()
intervals = [[1,5]]
newInterval = [2,3]

print(sol.insert(intervals,newInterval))