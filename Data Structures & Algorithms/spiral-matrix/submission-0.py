class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left = top = 0
        down, right = m-1, n-1
        res = []
        while len(res) < m*n:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top+1, down+1):
                res.append(matrix[i][right])
            if top != down:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[down][i])
            if left != right:
                for i in range(down-1, top, -1):
                    res.append(matrix[i][left])
            top += 1
            left += 1
            right -= 1
            down -= 1
        return res
            
        