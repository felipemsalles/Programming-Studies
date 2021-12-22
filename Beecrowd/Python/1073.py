# 1073
n = int(input())
if 5 < n < 2000:
    for i in range(2, n + 1, 2):
        print("{}^{} = {}".format(i, 2, i ** 2))