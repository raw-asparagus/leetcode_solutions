class Solution:
    #   ===========
    #   Two Pointer
    #   ===========

    #   Shift the left pointer and the right
    #   pointer towards each other until they
    #   meet. Each pointer tracks the max height
    #   encountered and increments accum by the
    #   difference in heights for 'valleys'
    def trap(self, height: List[int]) -> int:
        accum = 0             #   Accumulator
        
        i = 0
        left_max = height[0]
        j = len(height) - 1
        right_max = height[j]

        while (i < j):
            if (left_max < right_max):
                i += 1
                left_max = (height[i], left_max)[left_max > height[i]]
                accum += left_max - height[i]
            else:
                j -= 1
                right_max = (height[j], right_max)[right_max > height[j]]
                accum += right_max - height[j]
    
        return accum
