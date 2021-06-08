def sum(*no):
    sum = 0
    for i in no:
        sum += i
    return sum

rs = sum(987,345)
print(rs)

ars = sum(123,654,7890)
print(ars)
