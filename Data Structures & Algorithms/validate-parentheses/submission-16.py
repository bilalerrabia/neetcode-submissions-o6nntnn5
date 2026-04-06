class Solution:
    def isValid(self, s: str) -> bool:
        opens = "{(["
        closes = "})]"
        lst = []
        for i in s:
            if i in opens:
                lst.append(i)
            elif i in closes:
                if not lst:
                    return False
                last = lst.pop()
                if i == "}" and last != "{":
                    return False
                if i == "]" and last != "[":
                    return False
                if i == ")" and last != "(":
                    return False
            print(lst)
        if lst:
            return False
        return True