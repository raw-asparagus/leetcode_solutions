class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        j_len = len(board)
        i_len = len(board[0])
        
        word_len = len(word)

        def search_next(j: int, i: int, idx: int):
            #   Terminating case
            if idx == word_len:
                return True
            
            #   Boundary terminating cases
            elif (i < 0) or (i >= i_len) or (j < 0) or (j >= j_len):
                return False
            
            #   Current iterated value
            temp = board[j][i]

            #   Terminate current branch if doesn't extend word
            if temp != word[idx]:
                return False
            else:
                #   Change to invalid value after found so
                #   recursive calls doesn't branch to same cell
                board[j][i] = '!'

                #   Recursively branches to next cells
                next = idx + 1
                top = search_next(j - 1, i, next)
                bottom = search_next(j + 1, i, next)
                left = search_next(j, i - 1, next)
                right = search_next(j, i + 1, next)

                #   Restore value after recursive calls
                board[j][i] = temp

                #   Only returns 'True' if one of the branches
                #   returns 'True'
                return top or bottom or left or right
            
        for i in range(i_len):
            for j in range(j_len):
                #   Terminate if recursive calls finds full word
                if search_next(j, i, 0):
                    return True

        return False
