from typing import List
import math

def majorityElement(nums: List[int]) -> int:
    nums.sort();
    if not nums:
        return 0

    N = len(nums);
    nb = math.floor(N/2);
    k = nb;

    for i in range(nb,N):
        if nums[i] != nums[k-nb]:
            nums[k] = nums[i];
            k = k+1
    return nums[0]

nums = [3,3,4];
print(majorityElement(nums))