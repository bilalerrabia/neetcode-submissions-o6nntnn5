class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = len(s) - 1
        j = 0
        while i >= j:
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp
            j += 1
            i -= 1