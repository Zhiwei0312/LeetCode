# python list:
# use "=": 是同一个对象
# 浅拷贝：复制list要用 a.copy() / b = a[:] / b = list(a)
# 深拷贝：2D list 用浅拷贝，内层list没复制，要用import copy;b = copy.deepcopy(a)

class Solution: 
    # 注意左右
    # 取余操作
# O(n), O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        backup = nums.copy()

        for i in range(N):
            nums[(i + k) % N] = backup[i]

# “我把数组分成前 n−k 和后 k 两段，
# 通过整体反转把后段移到前面，
# 再分别反转两段恢复内部顺序，
# 最终得到右旋结果，时间 O(n)，空间 O(1)。
# reverse(A B) = (reverse(B) reverse(A))

# O(n-k), O(k)
    def rotate_3reverse(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n <= 1:
            return
        k %= n
        if k == 0:
            return

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# 原下标 i → 新下标 (i + k) % n
# 0 → 3 → 6 → 2 → 5 → 1 → 4 → 0
# 所有下标连成 一个大环，环长度 = 7（正好是 n）
# 我手里拿着一个值，一直往它该去的地方放，
# 被顶出来的那个，再继续拿在手里往下一个位置放
# O(n), O(1)
    def rotate_cycle(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n <= 1:
            return
        k %= n
        if k == 0:
            return

        moved = 0
        start = 0

        while moved < n:
            cur = start
            prev = nums[start]

            while True:
                nxt = (cur + k) % n
                nums[nxt], prev = prev, nums[nxt]
                cur = nxt
                moved += 1

                if cur == start:
                    break

            start += 1