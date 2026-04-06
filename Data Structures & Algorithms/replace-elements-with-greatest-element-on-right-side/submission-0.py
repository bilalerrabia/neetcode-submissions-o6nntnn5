class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for index in range(len(arr)):
            to_lock = index + 1
            if to_lock == len(arr):
                arr[-1] = -1
                return arr
            _max = arr[to_lock]
            while to_lock < len(arr):
                if arr[to_lock] > _max:
                    _max = arr[to_lock]
                to_lock += 1
            arr[index] = _max
        return arr
                

        