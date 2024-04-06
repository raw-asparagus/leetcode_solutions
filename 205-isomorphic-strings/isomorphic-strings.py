class Solution:
    #   ========
    #   Hash Map
    #   ========

    #   Store s's image in t and the inverse t's
    #   image in s in 2 hashmaps. Returns False
    #   if a t -> s mapping already exists or
    #   if there's a mismatched s -> t map
    def isIsomorphic(self, s: str, t: str) -> bool:
        swap = {}
        inverse = {}

        for idx, val in enumerate(s):
            if val not in swap:
                if t[idx] not in inverse:
                    swap[val] = t[idx]
                    inverse[swap[val]] = val
                    continue
                
                #   t -> s map already exists
                return False
            
            if swap[val] != t[idx]:
                return False

        return True
            

        