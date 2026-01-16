from typing import List

def removeDuplicates(nums: List[int]) -> int:
    N = len(nums)
    if N <= 2:
        return N

    k = 2  # 下一个写入位置（前两个一定保留）
    for i in range(2, N):

        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            print(i,k,nums)
            k += 1

    return k

nums = [1,1,1,2,2,3];
k = removeDuplicates(nums);
print(nums)