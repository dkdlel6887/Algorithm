tc = int(input())
vps_lst = list(input() for _ in range(tc))

def check_vps(vps):
    acnt, bcnt = 0, 0
    for i in range(len(vps)):
        if vps[i] == '(' and acnt >= bcnt:
            acnt += 1
        elif vps[i] == ')' and acnt > bcnt:
            bcnt += 1
        else:
            return 'NO'
    if acnt == bcnt:
        return 'YES'
    else:
        return 'NO'
for vps in vps_lst:
    print(check_vps(vps))