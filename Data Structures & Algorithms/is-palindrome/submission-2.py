class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst: list = [car.lower() for car in s if car.isalpha() or car.isnumeric()]
        i = 0
        j = len(lst) - 1
        while i < j:
            if lst[i] != lst[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
        