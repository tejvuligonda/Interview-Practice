# You are given a sorted list of distinct integers from 0 to 99, for instance [0, 1, 2, 50, 52, 75]. Your task is to produce a string that describes numbers missing from the list; in this case "3-49,51,53-74,76-99".
# Examples:
# [] “0-99”
# [0] “1-99”
# [3, 5] “0-2,4,6-99”

# Link: https://www.careercup.com/question?id=5753739085348864

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





