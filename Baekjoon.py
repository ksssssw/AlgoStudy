# name = input()
# if name == 'joonas':
#     print(name+'??!')

################################################

# year = input()
# print(int(year) - 543)

################################################

# resultList = []
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     resultList.append(a + b)

# for i in resultList:
#     print(i)

################################################

# resultList = []
# while True:
#     try:
#         a, b = list(map(int, input().split()))
#         resultList.append(a + b)
#     except:
#         break

# for i in resultList:
#     print(i)

################################################

# num = input()
# new_num = '-1'
# cnt = 0
# temp = num

# while True:
#     if int(num) == int(new_num):
#         break

#     if int(temp) < 10:
#         temp = '0' + temp
    
#     new_num = temp[-1] + str(int(temp[0]) + int(temp[-1]))[-1]
#     temp = new_num
#     cnt += 1
# print(cnt)

################################################

def solution(N, numberList):
    print('{} {}'.format(min(numberList), max(numberList)))

N = int(input())
numberList = list(map(int, input().split(' ')))
print(numberList)
solution(N, numberList)