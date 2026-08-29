class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        sub_box_map = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    continue
                box_num = (r//3, c//3)
                if num in row_map[r] or num in col_map[c] or num in sub_box_map[box_num]:
                    return False
                row_map[r].add(num)
                col_map[c].add(num)
                sub_box_map[box_num].add(num)
        return True