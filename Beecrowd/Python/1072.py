# 1072
n = int(input())
sum = 0
out = 0
for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        sum += 1
    else:
        out += 1
print("{} in".format(sum))
print("{} out".format(out))