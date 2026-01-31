# a variable for direction recording
# a matrix for visiting recording
# 表述清楚四个方向和限制条件就出来了

from typing import List 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows,cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]

        total = rows * cols
        output = [0] * total

        directions = [[0, 1],
                      [1, 0],
                      [0, -1],
                      [-1, 0]]
        row,col = 0,0
        directionIdx = 0

        for i in range(total):
            output[i] = matrix[row][col]
            visited[row][col] = True
            nextRow, nextCol = row + directions[directionIdx][0], col + directions[directionIdx][1]
            # print("nextRow, nextCol, rows, cols= ",nextRow, nextCol,rows, cols)
            # print("0 <= nextRow < rows = ",0 <= nextRow < rows)
            # print("0 <= nextCol < cols = ",0 <= nextCol < cols)
            # print("0 <= nextRow < rows and 0 <= nextCol < cols and not visited[nextRow][nextCol] = ",0 <= nextRow < rows and 0 <= nextCol < cols and not visited[nextRow][nextCol])
            if not(0 <= nextRow < rows and 0 <= nextCol < cols and not visited[nextRow][nextCol]):
                directionIdx = (directionIdx + 1) % 4
            row += directions[directionIdx][0]
            col += directions[directionIdx][1]
            # print("row,col = ",row,col)

        return output
    
    # 周围画圈
    def spiralOrder_another(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rows, columns = len(matrix), len(matrix[0])
        order = []
        left, right, top, bottom = 0, columns - 1, 0, rows - 1

        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])

            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])

            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return order
  
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = sol.spiralOrder(matrix)
print(result)