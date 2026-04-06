class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        for i in range(len(flowerbed)):
            if i + 1 == len(flowerbed):
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    counter += 1
                    break
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    counter += 1
                    continue
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                counter += 1
                flowerbed[i] = 1
        return n <= counter
