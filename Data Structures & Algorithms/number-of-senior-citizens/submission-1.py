class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([i for i in details if i[11] > "6" or i[11: 13] > "60"])
        