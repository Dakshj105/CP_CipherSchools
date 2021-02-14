def TrappringRainwaterProblem(li):
    left = [0] * len(li)
    right = [0] * len(li)

    left[0] = li[0]
    for i in range(1, len(li)):
        left[i] = max(left[i - 1], li[i])

    right[len(li) - 1] = li[len(li) - 1]
    for i in range(len(li) - 2, -1, -1):
        right[i] = max(right[i + 1], li[i])

    total = 0
    for i in range(len(li)):
        total += min(left[i], right[i]) - li[i]

    return total

li = list(map(int, input().split()))
amount = TrappringRainwaterProblem(li)
print(amount)