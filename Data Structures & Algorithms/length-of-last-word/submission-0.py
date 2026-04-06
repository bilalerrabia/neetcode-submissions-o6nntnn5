class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        lst = s.split()
        return len(lst[-1])
        