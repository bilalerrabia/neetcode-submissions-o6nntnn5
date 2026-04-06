class Solution:
    def isValid(self, s: str) -> bool:
        open_ = "[{("
        close_ = ")}]"

        lst = []
        for car in s:
            if car in open_:
                lst.append(car)
            if car in close_:
                if not lst:
                    return False
                car_tmp = lst.pop()
                if car == "]" and car_tmp != "[":
                    return False
                if car == ")" and car_tmp != "(":
                    return False
                if car == "}" and car_tmp != "{":
                    return False
        return not lst