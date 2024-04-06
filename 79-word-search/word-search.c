//  ==================
//  Depth-First Search
//  ==================

//  Performs DFS starting from each iterated cell
//  until each DFS branch is fully searched and
//  terminated (no possible new branch)

bool dfs(char**, int, int, int, int*, int, char*);

bool exist(char** board, int boardSize, int* boardColSize, char* word) {

    for (int j = 0; j < boardSize; j++) {
        for (int i = 0; i < *boardColSize; i++) {
            if (dfs(board, i, j, boardSize,boardColSize, 0, word))
                return 1;
        }
    }

    return 0;
}

bool dfs(char** board, int i, int j, int boardSize, int* boardColSize, int idx, char* word) {
    //  Success
    if (word[idx] == 0)
        return 1;
    //  Terminating case: boundary
    else if (i < 0 || i >= *boardColSize || j < 0 || j >= boardSize)
        return 0;
    
    int temp = board[j][i];

    //  Termiantign case: wrong letter
    if (temp != word[idx])
        return 0;

    //  Mask checked cell in new branch
    board[j][i] = 33;

    idx++;
    int top = dfs(board, i, j - 1, boardSize, boardColSize, idx, word);
    int bottom = dfs(board, i, j + 1, boardSize, boardColSize, idx, word);
    int left = dfs(board, i - 1, j, boardSize, boardColSize, idx, word);
    int right = dfs(board, i + 1, j, boardSize, boardColSize, idx, word);

    //  Unmask checked cell after branching
    board[j][i] = temp;

    return top + bottom + left + right;
}