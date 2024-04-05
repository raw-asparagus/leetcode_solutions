class Solution:
    #   Using the shortest string in strs as
    #   reference, iterate through every
    #   character and return on mismatch
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #   Base case
        if len(strs) == 1:
            return strs[0]

        ref = min(strs, key = len)

        for idx, val in enumerate(ref):
            for string in strs:
                if string[idx] != val:
                    return ref[:idx]

        #   Terminating case: strs is homogeneous
        return ref
