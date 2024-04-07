class Solution:
    #   Increment/decrement counts of '(', ')'
    #   and '*'. Return false on missing '('
    #   assuming '*' are '(' in main loop
    def checkValidString(self, s: str) -> bool:
        min_p = max_p = 0

        for i in s:
            match i:
                case '(':
                    min_p += 1
                    max_p += 1
                case ')':
                    min_p -= 1
                    max_p -= 1
                    #   If there are no preceding
                    #   '(' or '*'
                    if max_p < 0:
                        return False
                case _:
                    #   '*' as ')' if 
                    min_p -= 1
                    max_p += 1  #   '*' as '('

            #   Since max_p >= 0, every preceding
            #   ')' has a paired '(' and this is
            #   a valid check to prevent 'over-
            #   closing' of '('
            min_p = max(0, min_p)

        return not min_p
