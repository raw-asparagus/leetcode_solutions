class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #   Use first element as reference
        ref = strs[0]

        #   Base case:  'strs' only has 1 element
        if len(strs) == 1:
            return ref

        #   Checks all prefix combinations in reference
        for i in range(len(ref)):
            for i_str in strs[1:]:
                #   Terminating case if next iterating
                #   string lacks prefix combination
                if i_str[:i + 1] != ref[:i + 1]:
                    #   Returns previous prefix
                    #   combination
                    return ref[:i]

        #   Trivial case:  'strs' is homogeneous
        return ref
        