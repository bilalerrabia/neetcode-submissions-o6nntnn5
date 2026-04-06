class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for ith in logs:
            if ith == "../":
                counter -= 1
                if counter < 0:
                    counter = 0
            elif ith != "./":
                counter += 1
        if counter < 0:
            return 0
        return counter
        