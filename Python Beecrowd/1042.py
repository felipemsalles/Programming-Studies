# 1042
option = input().split(" ")
values = [int(i) for i in option]

values.sort()
print(*values, sep='\n')
print()
print(*option, sep='\n')
