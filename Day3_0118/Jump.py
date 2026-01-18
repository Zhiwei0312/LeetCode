# 把每一次跳跃看成“一层覆盖范围”
# 在当前跳跃范围内，尽量把下一跳能覆盖的最远位置推到最大
# 当扫描到当前范围的边界时，必须跳一次

# steps：已经用了多少次跳跃
# current_end：当前这一次跳跃能覆盖到的最远位置
# farthest：在当前覆盖范围内，下一次跳跃能到的最远位置

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                steps += 1
                current_end = farthest

        return steps