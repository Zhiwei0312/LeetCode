from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotate 90 deg <==> transpose
        auxiliaryMatrix = matrix.copy()
        N = len(matrix)

        for i in range(N):
            matrix[i] = [x[i] for x in auxiliaryMatrix[::-1]]
            print(matrix[i])

    def rotate_inplace(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

# transpose = 水平翻转 + 主对角线反转
    def rotate_flip(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
sol.rotate(matrix)
print(matrix)