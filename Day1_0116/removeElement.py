# 27

# 双指针

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # 慢指针：下一个要写的位置

        for i in range(len(nums)):  # 快指针
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# raw answer
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         N = nums.length; # this is a list, not a numpy array
        
#         k = 0;
#         for i = 0:N-1: # this is Python, should be for i in range(N)
#             if nums[i] == val:
#                 nums[k] = nums[i+1]; # the logic is wrong, instead of searching for 
#                 # elements to be removed, search for elements to keep
#             else:
#                 nums[k] = nums[i];
#                 k = k + 1;