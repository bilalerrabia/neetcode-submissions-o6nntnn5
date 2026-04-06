class Solution:
    def isValid(self, s: str) -> bool:
        opens = "({["
        closes = ")}]"
        lst = []
        if s[0] in closes or s[len(s) - 1] in opens:
                return False
        for car in s:
            if car in opens:
                lst.append(car)
                continue
            if len(lst) == 0 and car in closes:
                return False
            if car in closes and len(lst) != 0:
                if car == ")" and lst[-1] != "(":
                    return False
                elif car == "}" and lst[-1] != "{":
                    return False
                elif car == "]" and lst[-1] != "[":
                    return False
                else:
                    lst.pop()
            
        if len(lst) == 0:
            return True
        return False

        