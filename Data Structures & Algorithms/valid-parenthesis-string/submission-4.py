class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                star.append(i)
            else: 
                if len(left) > 0: 
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        # match each left with * 
        while len(left) > 0: 
            l = left.pop() 
            if len(star) == 0:
                return False
            r = star.pop()
            if r < l:
                return False
        return True

        # when ), pop off left, if left empty, pop off star, if star empty, return False