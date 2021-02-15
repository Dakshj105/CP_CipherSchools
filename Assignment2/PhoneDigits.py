def PhoneDigitsMain(n):
    n1 = []
    l = 0
    for i in n:
        if d[i]:
            n1.append(i)
            l += 1
    PhoneDigits(n1, l)
def PhoneDigits(n, l, lis = [], cur = 0):
  
        if cur == l:
            print("".join(lis), end = " ")
            return
    
        for i in range(len(d[n[cur]])):
            lis.append(d[n[cur]][i])
            PhoneDigits(n, l, lis, cur + 1)
            lis.pop()


n = [int(i) for i in input()]
d = {1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz", "*":"", 0:"", "#":""}
PhoneDigitsMain(n)