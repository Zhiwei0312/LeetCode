from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)

        if N == 0:
            return []
        elif N == 1:
            return [str(nums[0])]

        prev = nums[0]
        a = [prev];b = []
        for i in range(1,N):
            curr = nums[i]

            if curr != prev + 1:
                b.append(prev)
                a.append(curr)
            prev = curr
        b.append(prev)

        N = len(a)
        output = []
        for i in range(N):
            if a[i] == b[i]:
                output.append(str(a[i]))
            else:
                output.append(str(a[i])+"->"+str(b[i]))
        return output
    
sol = Solution()

nums = [0,1,2,4,5,7]
result = sol.summaryRanges(nums)
print(result)
