class Solution:
    #   Increment/decrement count on '(' / ')',
    #   tracking max in max_count
    def maxDepth(self, s: str) -> int:
        max_count = count = 0

        for char in s:
            if char == "(":
                count += 1
                max_count = max(count, max_count)
            elif char == ")":
                count -= 1
        
        return max_count
        