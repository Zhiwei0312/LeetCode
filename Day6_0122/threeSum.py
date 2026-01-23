from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        answer = []
        
        for i in range(N):
            if i>0 and nums[i] == nums[i-1]: # 去重
                continue
            if nums[i] > 0:
                break
            left, right = i+1, N-1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    answer.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1


        return answer

sol = Solution()

nums = [-1, 3,-2]
result = sol.threeSum(nums)
print(result)
        