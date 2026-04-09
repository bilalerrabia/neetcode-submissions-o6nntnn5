class Solution:
    def ana_7mare(self, my_list):
        print(my_list)
        i, j = 0, len(my_list) - 1
        while j > i:
            if my_list[i] != my_list[j]:
                return False
            i += 1
            j -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        my_list = list(s)
        # if len(my_list) <= 2:
        #     return True
        # dct = {k : my_list.count(k) for k in my_list}
        # count = 0
        # lonly_car = "="
        # for car in my_list:
        #     if dct[car] % 2 != 0 and car != lonly_car:
        #         count += 1
        #         lonly_car = car
        #         print(car)
        # if count > 2:
        #     return False
        # elif count != 0:
        #     my_list.remove(lonly_car)
        for i in range(len(my_list)):
            tmp = my_list.copy()
            tmp.pop(i)
            if self.ana_7mare(tmp):
                return True
        return False

        
