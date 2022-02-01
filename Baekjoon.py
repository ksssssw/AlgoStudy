# name = input()
# if name == 'joonas':
#     print(name+'??!')

# year = input()
# print(int(year) - 543)

resultList = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    resultList.append(a + b)

for i in resultList:
    print(i)
    
