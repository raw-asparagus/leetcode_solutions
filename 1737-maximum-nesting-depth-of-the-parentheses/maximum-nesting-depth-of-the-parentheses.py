class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        #   Accumulator
        #   - increment when '('
        #   - decrement when ')'
        count = 0

        max_count = 0   #   Max of count

        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            
            if count > max_count:
                #   when 'count' overtakes
                #   'max_count'
                max_count += 1
        
        return max_count
        