from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        hash = {}
        Count = {}

        for i in range(N):
            hash[nums[i]] = i
            Count[nums[i]] = Count.get(nums[i],0) + 1

        for i in range(N):
            diff = target - nums[i]
            Count[nums[i]] -= 1;
            if Count.get(diff,0):
                return [i, hash[diff]]

        return [-1, -1]

sol = Solution()
nums = [3,2,4]
targets = 6

result = sol.twoSum(nums,targets)
print(result)