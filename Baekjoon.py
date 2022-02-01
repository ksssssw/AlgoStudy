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

# def solution(N, numberList):
#     print('{} {}'.format(min(numberList), max(numberList)))

# N = int(input())
# numberList = list(map(int, input().split(' ')))
# solution(N, numberList)

################################################
# temp = []
# for i in range(9):
#     a = int(input())
#     temp.append(a)

# print(max(temp))
# print(temp.index(max(temp)) + 1)

################################################
# input_List = [int(input()) for x in range(0, 3)]
# temp = str(input_List[0] * input_List[1] * input_List[-1])

# for i in range(0, 10):
#     print(temp.count(str(i)))

################################################
# result_List = []
# input_List = [int(input()) for x in range(0, 10)]

# for i in input_List:
#     result_List.append(i % 42)

# print(len(set(result_List)))

################################################
# p = int(input())
# orginal_score = list(map(int, input().split(' ')))
# m = max(orginal_score)
# new_score = [x/m*100 for x in orginal_score]
# print(sum(new_score) / p)

################################################
# p = int(input())
# score_list = [input() for x in range(p)]
# result_list = []

# for i in score_list:
#     score = 0
#     temp = 0
#     for j in i:
#         if j == 'O':
#             temp += 1
#             score += temp
#         else:
#             temp = 0
#             score += temp
#     result_list.append(score)

# for i in result_list:
#     print(i)

################################################
p = int(input())
class_list = [list(map(int, input().split())) for x in range(p)]
result_list = []

for i in class_list:
    cnt = 0
    class_avg = sum(i[1:]) / i[0]
    for score in i[1:]:
        if score > class_avg:
            cnt += 1
        else:
            pass
    result_list.append('%.3f%%' % (cnt/i[0]*100.0))

for i in result_list:
    print(i)
