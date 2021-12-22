# 1019
num = int(input())
seconds = [3600, 60, 1]
result = []
for i in seconds:
    quantity = int(num / i)
    result.append(str(quantity))
    num -= quantity * i

print(":".join(result))