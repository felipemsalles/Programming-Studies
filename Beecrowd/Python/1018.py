# 1018
value = int(input())
print(value)
ballots = [100, 50, 20, 10, 5, 2, 1]
for ballot in ballots:
    qty_ballots = int(value / ballot)
    print('{} nota(s) de R$ {},00'.format(qty_ballots, ballot))
    value -= qty_ballots * ballot


# notas (Portuguese) = ballots (English)