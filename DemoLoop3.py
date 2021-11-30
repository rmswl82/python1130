# DemoLoop3.py

lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))


print("---수열함수---")

result = list(range(10))
print(result)
result = list(range(1,11))
print(result)

years = list(range(2000, 2022))
print(years)

#수동으로 루프를 돌리는 경우

for i in range(5):
    print(i)

#리스트 함축(리스트 내장, 압축)

lst = list(range(1,11))
result2 = [i**2 for i in lst if i >5]
print(result2)

tp = ("apple", "banan]a", "orange")
print(tp)
print([len(i) for i in tp])

d = {100:"apple", 200:"orange", 300:"kiwi"}
print( [v.upper() for v in d.values()])

