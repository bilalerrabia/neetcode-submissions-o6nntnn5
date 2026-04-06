class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cars = "abcdefjhigklmnopqrstuvwxyz"
        lst_1: dict = {car : 0 for car in cars}
        lst_2: dict = {car: 0 for car in cars}
        for car in s:
            lst_1[car] += 1
        for car in t:
            lst_2[car] += 1
        return lst_1 == lst_2
        