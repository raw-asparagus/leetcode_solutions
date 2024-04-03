class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        #   Iterate through nums for first operand
        for i in range(nums_len):
            #   Iterate through nums for second operand
            for j in range(i + 1, nums_len):
                #   Terminating case if i <= j
                #   For indices j smaller than i, we have already
                #   checked those pairs in previous iterations
                if nums[i] + nums[j] == target:
                    return [i, j]
