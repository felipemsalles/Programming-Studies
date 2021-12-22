# 1038
code, quantity = input().split(" ")
code = int(code)
quantity = int(quantity)
if code == 1:
    print("Total: R$ {0:.2f}".format(quantity * 4.00))
elif code == 2:
    print("Total: R$ {0:.2f}".format(quantity * 4.50))
elif code == 3:
    print("Total: R$ {0:.2f}".format(quantity * 5.00))
elif code == 4:
    print("Total: R$ {0:.2f}".format(quantity * 2.00))
elif code == 5:
    print("Total: R$ {0:.2f}".format(quantity * 1.50))