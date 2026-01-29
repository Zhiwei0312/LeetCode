# 每个气球是区间 [x_start, x_end]，一支箭在位置 x 可以打爆所有满足 x_start ≤ x ≤ x_end 的气球。
# 想让一支箭覆盖更多区间，最优策略是：
# 按区间右端点从小到大排序
# 放第一支箭在第一个区间的 end
# 继续看后面的区间：
# 如果 start ≤ current_end，说明这区间和当前箭位置有交集，同一支箭能打爆，跳过
# 否则必须新开一支箭，把箭位置更新为这个区间的 end
# 这是经典“最少点覆盖区间”问题。

# 为什么「原本引爆的气球仍然被引爆」是唯一的要求？
# 一定存在一种最优（射出的箭数最小）的方法，使得每一支箭的射出位置都恰好对应着某一个气球的右边界。



from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # 按右端点排序
        points.sort(key=lambda x: x[1])

        arrows = 1
        cur_end = points[0][1]

        for start, end in points[1:]:
            if start <= cur_end:
                # 还在当前箭覆盖范围内
                continue
            # 需要新箭
            arrows += 1
            cur_end = end

        return arrows
    

    def findMinArrowShots_left(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # 按右端点排序
        points.sort(key=lambda x: x[0],reverse = True)

        arrows = 1
        cur_start = points[0][0]

        for start, end in points[1:]:
            if end >= cur_start:
                # 还在当前箭覆盖范围内
                continue
            # 需要新箭
            arrows += 1
            cur_start = start

        return arrows