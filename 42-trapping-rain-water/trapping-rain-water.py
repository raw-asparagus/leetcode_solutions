class Solution:
    def trap(self, height: List[int]) -> int:
        acc = 0             #   Accumulator

        i = 0               #   Left
        left_max = height[i]
        j = len(height) - 1 #   Right
        right_max = height[j]
        while i < j:
            #   Right is taller
            if height[i] < height[j]:
                #   Next left is shorter than previous
                if height[i] < left_max:
                    acc += left_max - height[i]
                #   Next left is taller than previous
                else:
                    left_max = height[i]
                
                i += 1
            #   Left is taller or both are same height
            else:
                #   Previous right is shorter than next
                if height[j] < right_max:
                    acc += right_max - height[j]
                #   Previous right is taller than next
                else:
                    right_max = height[j]
                
                j -= 1
    
        return acc
