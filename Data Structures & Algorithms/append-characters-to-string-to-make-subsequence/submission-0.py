class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                j += 1
                i += 1
            else:
                i += 1
            if j == len(t):
                return 0
        return len(t) - j