from typing import List

# 构建两个数组L，R分别记录左右乘积
# O(N), O(N)
def productExceptSelf(nums: List[int]) -> List[int]:
    N = len(nums)
    L, R, answer = [1]*N, [1]*N, [1]*N


    for i in range(1,N):
        L[i] = L[i-1] * nums[i-1]

    for i in range(N-2,-1,-1):
        R[i] = R[i+1] * nums[i+1]

    for i in range(N):
        answer[i] = L[i] * R[i]

    return answer

nums = [1,2,3,4]
# print(productExceptSelf(nums))

# 用answer本身作L
# R数组用一个变量循环表示
# O(n), O(1)
def productExceptSelf_spatial1(self, nums: List[int]) -> List[int]:
    N = len(nums)
    answer = [1]*N


    for i in range(1,N):
        answer[i] = answer[i-1] * nums[i-1]

    R = 1;
    for i in range(N-1,-1,-1):
        answer[i] = answer[i] * R;
        R = R  * nums[i]

    return answer