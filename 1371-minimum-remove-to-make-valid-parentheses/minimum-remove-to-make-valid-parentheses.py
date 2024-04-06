class Solution:
    #   =====
    #   Stack
    #   =====

    #   Keeps a stack of indices of '(' and ')'
    #   to remove. If first parentheses is ')' or
    #   successive parentheses is '(', append to
    #   stack. Only successive paired '('-')'
    #   will remove appended '(' from stack
    #   Excess '(' and unmatched initial ')' will
    #   remain in the stack at the end of the
    #   iteration
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for idx, val in enumerate(s):
            if val == ")":
                stack.pop() if stack and s[stack[-1]] == "(" else stack.append(idx)
            elif val == "(":
                stack.append(idx)

        return_str = "".join(( s[i] for i in range(len(s)) if i not in stack ))
        
        return return_str     
        