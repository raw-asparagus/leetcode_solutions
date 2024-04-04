class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        #   Iterate through nums for first operand, then iterate through nums for second operand
        #   excluding iterated first operands
        nums_len = len(nums)

        for i in range(nums_len):
            #   Start at index at least 'indexDifference' away
            for j in range(i + indexDifference, nums_len):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        
        #   Default
        return  [-1, -1]
        