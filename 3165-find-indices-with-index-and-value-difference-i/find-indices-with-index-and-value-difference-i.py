class Solution:
    #   Iterate through nums, returns iterated
    #   num and nested iterated num pair if both
    #   num fulfill conditions
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i_idx, i_val in enumerate(nums):
            for j_idx, j_val in enumerate(nums[i_idx + indexDifference:], start = i_idx + indexDifference):
                if abs(i_val - j_val) >= valueDifference:
                    return [i_idx, j_idx]
        
        #   Default
        return  [-1, -1]
        