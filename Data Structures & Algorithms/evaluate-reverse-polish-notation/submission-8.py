class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        for i in tokens:
            if i == "*":
                num2 = lst.pop()
                num1 = lst.pop()
                lst.append(int(num1) * int(num2))
            elif i == "+":
                num2 = lst.pop()
                num1 = lst.pop()
                lst.append(int(num1) + int(num2))
            elif i == "-":
                num2 = lst.pop()
                num1 = lst.pop()
                lst.append(int(num1) - int(num2))
            elif i == "/":
                num2 = lst.pop()
                num1 = lst.pop()
                lst.append(int(num1) / int(num2))
            else:
                lst.append(i)
            print(lst)
        return int(lst[0])
            

