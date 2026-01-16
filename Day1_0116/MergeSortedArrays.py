# note: 考虑边界条件。

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1          # nums1 有效部分末尾
        j = n - 1          # nums2 末尾
        k = m + n - 1      # nums1 最末尾（填充位置）

        # 当 nums2 还有元素没合并完，就继续
        while j >= 0:
            # nums1 还有有效元素且 nums1[i] 更大 -> 放 nums1[i]
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# raw soluiton:
class Solution: 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        """ Do not return anything, modify nums1 in-place instead. """ 
        num1_idx = m-1; 
        mnum2_idx = n-1; 
        for xx = m+n-1:0:
            if nums1[num1_idx] >= nums2[num2_idx]: 
                ums1[xx] = nums1[num1_idx]; 
                num1_idx = num1_idx - 1; 
            else:
                nums1[xx] = nums2[num2_idx]; 
                num2_idx = num2_idx - 1;