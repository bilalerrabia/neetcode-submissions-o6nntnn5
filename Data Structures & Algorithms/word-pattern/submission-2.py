class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        s = s.split()
        lst = {}
        for car, word in zip(pattern, s):
            if lst.get(car, "__") == "__":
                lst[car] = word
                continue
            elif lst.get(car) != word:
                return False
        for i, index1 in enumerate(lst.values(), 0):
            for j, index2 in enumerate(lst.values(), 0):
                print(index1, i)
                if i == j:
                    continue
                if index1 == index2:
                    return False
        return True
        