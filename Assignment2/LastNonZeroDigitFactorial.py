def calc2spower(n):
    s = "6248"
    return int(s[n % 4]) if n != 0 else 1

def LastNonZeroDigitFactorial(n):
    if n == 0:
        return 1
    if 1 <= n <= 4:
        s= '1264'
        return int(s[n - 1])

    a = n // 5
    b = n - a * 5
    
    return (calc2spower(a) * LastNonZeroDigitFactorial(a) * LastNonZeroDigitFactorial(b)) % 10

n = int(input())
print(LastNonZeroDigitFactorial(n))


