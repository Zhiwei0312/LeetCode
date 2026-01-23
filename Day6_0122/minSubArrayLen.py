from typing import List

# 滑动窗口法
# O(n): left and right指标最多滑动n次
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        sumData = 0
        minStep = inf;
        for right in range(N):
            sumData += nums[right]
            # print("left, right, sum = ", left, right, sumData)

            while sumData >= target:
                minStep = min(minStep, right - left + 1)
                # print("sumData, left, right, minStep = ",sumData,left,right,minStep)
                sumData -= nums[left]
                left += 1
        return 0 if minStep == inf else minStep

nums = [12,28,83,4,25,26,25,2,25,25,25,12]
sol = Solution()
result = sol.minSubArrayLen(213,nums)
print(result)
print(sum([25, 25, 25, 25, 26, 28, 83]))