def MinimumPlatform(arrival, departure):
    cur_platform = max_platform = 0
    i = j = 0
    while(i < len(arrival)):
        if arrival[i] < departure[j]:
            cur_platform += 1
            i += 1

        else:
            cur_platform -= 1
            j += 1

        if cur_platform > max_platform:
            max_platform = cur_platform

    return max_platform


arr = list(map(int, input().split()))
dep = list(map(int, input().split()))
arr.sort()
dep.sort()
print(MinimumPlatform(arr, dep))