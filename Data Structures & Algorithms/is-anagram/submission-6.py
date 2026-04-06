class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s = [0 for _ in range(26)]
        lst_t = [0 for _ in range(26)]
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            lst_s[ord(i) - ord("a")] += 1
            lst_t[ord(j) - ord("a")] += 1
        print(lst_s)
        print(lst_t)
        return lst_s == lst_t
        