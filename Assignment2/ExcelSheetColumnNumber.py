def ExcelSheetColumnNumber(s):
    if len(s) == 0:
        return
    if len(s) == 1:
        print(ord(s) - 64)
    c = [26]
    ColumnNumber(s, c)
    print(c[0])

def ColumnNumber(s, c):
    if len(s) == 1:
        c[0] += ord(s) - 64
        return
    
    c[0] *= (ord(s[0]) - 64)
    ColumnNumber(s[1:], c)


s = input()
ExcelSheetColumnNumber(s)