class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lst = {}
        for i in range(len(s)):
            if lst.get(s[i], "__") == "__":
                lst[s[i]] = t[i]
            elif lst.get(s[i]) != t[i]:
                return False
        print(lst)
        print(lst.values())
        for i, index1 in enumerate(lst.values(), 0):
            for j, index2 in enumerate(lst.values(), 0):
                if i == j:
                    print("skip")
                    print(index1, index2)
                    print(i, j)
                    continue
                if index1 == index2:
                    return False
        return True