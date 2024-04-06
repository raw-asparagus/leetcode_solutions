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
            match val:
                case ")":
                    stack.pop() if stack and s[stack[-1]] == "(" else stack.append(idx)
                case "(":
                    stack.append(idx)

        return_str = "".join([ val for idx, val in enumerate(s) if idx not in stack ])
        
        return return_str     
        