class Solution:
    #   ===========================
    #   Stack -- Last in, First out
    #   ===========================

    #   Pop last and skip next if next-last pair
    #   makes the string bad, else appends next
    #   character
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for i in s[1:]:
            if stack and abs(ord(stack[-1]) - ord(i)) == 32:
                stack.pop()
                continue

            stack.append(i)

        return "".join(stack)
