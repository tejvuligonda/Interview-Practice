def approachOne(arr):
    missing = set()
    for i in range(100):
        missing.add(i)
    given = set(arr)
    missin = missing - given
    result = ''
    high = 0
    low = 0
    missin = sorted(list(missin))
    if missin:
        low = missin[0]
    for i in range(len(list(missin))):
        high = missin[i]
        if (i == len(missin) - 1) or (missin[i+1] - missin[i] > 1):
            if low == high:
                temp = str(low) + ','
            else:
                temp = str(low) + '-' + str(high) + ','
            result += temp
            if (i != len(missin) - 1):
                low = missin[i+1]
    return result[:-1]

print(approachOne([]))
print(approachOne([5]))
print(approachOne([0, 1, 2, 50, 52, 75]))





