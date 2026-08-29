class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        subgrid_dict = defaultdict(set)
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == '.':
                    continue
                if num in row_dict[row] or num in col_dict[column] or num in subgrid_dict[(row//3,column//3)]:
                    return False
                row_dict[row].add(num)
                col_dict[column].add(num)
                subgrid_dict[(row//3, column//3)].add(num)
        return True
                