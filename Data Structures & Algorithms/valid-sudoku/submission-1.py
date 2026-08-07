class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        boxs=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                num=board[i][j]
                if num in row[i]:
                    return False
                row[i].add(num)
                if  num in col[j]:
                    return False
                col[j].add(num)
                box=(i//3)*3+j//3
                if num in boxs[box]:
                    return False
                boxs[box].add(num)
        return True




