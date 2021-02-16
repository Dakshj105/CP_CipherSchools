def GenerateValidIp(s):
    n = len(s)
    if n == 0 or n > 12:
        print("NO Valid Ip")
        return
    total_Ips = []
    IpValidChecker(s, total_Ips)
    if total_Ips:
        for i in total_Ips:
            print(i, end = " ")
    else:
        print("No Valid Ip")

def IpValidChecker(s, total_Ips, current_Ips = [""] * 4, cur = 0, Ip_cur = 0):
    
    if Ip_cur == 4 and cur == len(s):
        total_Ips.append(f"{current_Ips[0]}.{current_Ips[1]}.{current_Ips[2]}.{current_Ips[3]}")
        return
    
    elif Ip_cur == 4 or cur == len(s):
        return

    for i in range(1, 4):
        substring = s[cur: cur + i]
        if substring[0] == '0' or Ip_cur >=2 and int(substring) > 255:
            break
        current_Ips[Ip_cur] = substring
        IpValidChecker(s, total_Ips, current_Ips, cur + i, Ip_cur + 1)
        current_Ips[Ip_cur] = -1
        


s = input()
GenerateValidIp(s)