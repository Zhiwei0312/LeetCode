# s = set() 是一个“没有重复元素、没有顺序”的集合。
# s.add()
# s.remove() -- 不存在会报错
# s.discard() -- 删除
# set中不能放可变对象
# s.add([1,2])   # ❌ 错误
# s.add((1,2))   # ✅
# set() 是一个用于快速“去重 + 判断是否出现过”的无序集合，查找时间复杂度是 O(1)。

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Hash = set()
        N = len(nums)

        for i in range(min(k+1,N)):
            if nums[i] in Hash:
                return True
            else:
                Hash.add(nums[i])

        if k+1 < N:
            for i in range(k+1,N):
                Hash.remove(nums[i-k-1])
                if nums[i] in Hash:
                    return True
                else:
                    Hash.add(nums[i])
        return False

sol = Solution()

nums = [1,2,3,1]
k = 3

result = sol.containsNearbyDuplicate(nums,k)
print(result)