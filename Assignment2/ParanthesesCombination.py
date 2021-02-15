def ParanthesisCombination(lis, n, open_c = 0, close_c = 0, cur = 0):
    if n < 1:
        return
    elif close_c == n:
        print("".join(lis))
    elif open_c > close_c:
        lis[cur] = "}" 
        ParanthesisCombination(lis, n, open_c, close_c + 1, cur + 1)
    if open_c < n:
        lis[cur] = "{"
        ParanthesisCombination(lis, n, open_c + 1, close_c, cur + 1)

n = int(input())
ParanthesisCombination([""] * 2* n, n)