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
        for i in range(len(my_list)):
            tmp = my_list.copy()
            tmp.pop(i)
            if self.ana_7mare(tmp):
                return True
        return False

        
