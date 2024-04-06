class Solution:
    #   ========
    #   Hash Map
    #   ========

    #   Store every character in s and its map in
    #   t as a key-value pair in hashmap. Returns
    #   'False' on mismatched mapping
    def isIsomorphic(self, s: str, t: str) -> bool:
        swap = {}

        for idx, val in enumerate(s):
            if val not in swap:
                if t[idx] in swap.values():
                    return False
                
                swap[val] = t[idx]
                continue
            
            if swap[val] != t[idx]:
                return False

        return True
            

        