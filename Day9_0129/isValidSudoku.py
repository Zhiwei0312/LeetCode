# 用 set / hash table 每个元素检查三次，不要横着查一次，竖着查一次，block差一次，其实也是一样的，不过它写的干净一些
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]   # box index = (r//3)*3 + (c//3)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue

                b = (r // 3) * 3 + (c // 3)

                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)

        return True
    
class Solution_myself:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.isValidHorizontal(board):
            return False
        
        if not self.isValidVertical(board):
            return False

        if not self.isValidBlock(board):
            return False

        return True

    def isValidVertical(self,board:List[List[str]]) -> bool:
        N = len(board)
        for i in range(N):
            isValid = self.isValidVals(board[i])
            if not isValid:
                return False
        return True

    def isValidHorizontal(self,board:List[List[str]]) -> bool:
        N = len(board)
        data = []
        for i in range(N):
            data = [x[i] for x in board]
            isValid = self.isValidVals(data)
            if not isValid:
                return False
        return True

    def isValidBlock(self,board:List[List[str]]) -> bool:
        N = len(board)
        nBlock = int(N / 3)

        for i in range(nBlock):
            for j in range(nBlock):
                block = self.get_block(board,i,j)
                isValid = self.isValidVals(block)
                if not isValid:
                    return False
        return True

    def get_block(self, board:List[List[str]], br:int, bc:int) -> List[int]:
        # br, bc: block row/col index in {0,1,2}
        r0, c0 = br * 3, bc * 3
        return [board[r][c] for r in range(r0, r0 + 3) for c in range(c0, c0 + 3)]


    def isValidVals(self,vals:List[int]) -> bool:
        vals = [x for x in vals if x != "."]
        isValid = len(vals) == len(set(vals))
        return isValid
