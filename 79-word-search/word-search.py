class Solution:
    #   ==================
    #   Depth-First Search
    #   ==================

    #   Performs DFS starting from each iterated
    #   cell until each DFS branch is fully
    #   searched and terminated (no possible
    #   new branch)
    
    def exist(self, board: list[list[str]], word: str) -> bool:
        x = len(board[0])
        y = len(board)
        
        word_len = len(word)

        def dfs(i: int, j: int, idx: int) -> bool:
            #   Success
            if idx == word_len:
                return True
            #   Terminating case: boundary
            elif (i < 0) or (i >= x) or (j < 0) or (j >= y):
                return False
            
            temp = board[j][i]

            #   Terminating case: wrong letter
            if temp != word[idx]:
                return False
            
            #   Mask checked cell in new
            #   branch
            board[j][i] = '!'

            idx += 1
            top = dfs(i, j - 1, idx)
            bottom = dfs(i, j + 1, idx)
            left = dfs(i - 1, j, idx)
            right = dfs(i + 1, j, idx)

            #   Unmask checked cell after
            #   branching
            board[j][i] = temp

            #   Return branching result
            return top or bottom or left or right
            
        for i in range(x):
            for j in range(y):
                if dfs(i, j, 0):
                    return True

        return False
