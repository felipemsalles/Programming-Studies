# 1099
n = int(input())
for i in range(n):
    test = [int(num) for num in input().split(" ")]
    x = min(test)
    y = max(test)
    sum = 0
    for num in range(x + 1, y):
        if num % 2 != 0:
            sum += num
    print(sum)