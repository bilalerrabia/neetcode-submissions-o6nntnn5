class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        corrent = ''
        result = []

        while i < len(chars):
            local_counter = 0
            corrent = chars[i]
            while i < len(chars) and chars[i] == corrent:
                i += 1
                local_counter += 1
            if local_counter == 1:
                result.append(corrent)
            else:
                result.append(corrent)
                local_str = str(local_counter)
                for car in local_str:
                    result.append(car)
        print(result)
        for i in range(len(result)):
            chars[i] = str(result[i]) 
        return len(result)
