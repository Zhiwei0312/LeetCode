# 找到每个位置左边最大值和右边最大值
# 下标i处能接的雨水量等于下标i处的水能到达的最大高度减去height[i]
# 左右相交处是最大值

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0;
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n-1)

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans
