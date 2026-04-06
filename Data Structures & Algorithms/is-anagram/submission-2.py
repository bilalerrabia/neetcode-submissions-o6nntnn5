class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s = [0 for _ in range(26)]
        lst_t = [0 for _ in range(26)]

        for car in s:
            lst_s[ord(car) - ord("a")] += 1
        for car in t:
            lst_t[ord(car) - ord("a")] += 1

        for car1, car2 in zip(lst_s, lst_t):
            if car1 != car2:
                return False
        return True
        