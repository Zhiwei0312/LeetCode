from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for row in rows:
            matrix[row] = [0] * n

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0

    def setZeroes_saveSpace(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # 记录第一行或者第一列是否有0，有的话最后要全部清零
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        print("flag_col0, flag_row0 = ",flag_col0, flag_row0)
        
        # 用第一行/第一列记录这一行/列是否有0，有的话设为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # 根据第一行/列的0进行清零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 如果第一行/列有0，全部清零
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0


sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
sol.setZeroes_saveSpace(matrix)
print(matrix)