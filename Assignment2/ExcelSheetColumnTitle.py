def ExcelSheetColumnTitle(n):
    r = [""]
    ColumnTitle(n, r)
    print(r[0])

def ColumnTitle(n, r):
    if n == 0:
        return
    c = chr(ord("A") + (n - 1) % 26)
    r[0] = c + r[0]
    ColumnTitle((n - 1) // 26, r)

n = int(input())
ExcelSheetColumnTitle(n)
