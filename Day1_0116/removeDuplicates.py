from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # 慢指针：下一个写入位置

        for i in range(1, len(nums)):  # 快指针
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# wrong: want the number of unique values, not the number of time it duplicates
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums);
        k = 1;
        nb = 0;

        for i in range(1, N):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i];
                k = k + 1;
                nb = nb + 1;

        nums = nums[0:nb];
            
        k = len(nums);
        return k