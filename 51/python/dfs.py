class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols, diags1, diags2 = \
            [False for _ in range(n)], \
            [False for _ in range(2 * n - 1)], \
            [False for _ in range(2 * n - 1)]

        def available(x, y):
            #  x, y 是当前的坐标
            #  强剪枝，返回当前位置是否可以放置皇后
            return not cols[x] and not diags1[x + y] and not diags2[x - y + n - 1]

        def updateBoard(x, y, is_put):
            """
            更新棋盘 与 用于剪枝的constraint list（cols/diags1/diags2）
            :param x: 坐标
            :param y:
            :param is_put: boolean 类型
            """
            cols[x] = is_put
            diags1[x + y] = is_put
            diags2[x - y + n - 1] = is_put
            board[x][y] = 'Q' if is_put else '.'

        def n_queens(y):
            if y == n:
                board_copy = [''.join(_) for _ in board]
                res.append(board_copy)
                return
            for x in range(n):
                if not available(x, y): continue
                updateBoard(x, y, True)
                n_queens(y + 1)
                updateBoard(x, y, False)

        n_queens(0)
        return res


if __name__ == '__main__':
    s = Solution()
    qwer = s.solveNQueens(8)
    print(s.solveNQueens(8))
