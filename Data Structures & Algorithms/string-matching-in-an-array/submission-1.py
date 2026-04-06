class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = list()
        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                if word1 in word2:
                    res.append(word1)
        return list(set(res))