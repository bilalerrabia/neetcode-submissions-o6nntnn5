class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_leght = min([len(x) for x in strs])
        print(min_leght)
        i = 0
        while i < min_leght:
            res += strs[0][i]
            for j in strs:
                if j.startswith(res):
                    continue
                else:
                    return res[:-1]
            i += 1
        return res
