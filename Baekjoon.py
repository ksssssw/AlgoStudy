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
# p = int(input())
# class_list = [list(map(int, input().split())) for x in range(p)]
# result_list = []

# for i in class_list:
#     cnt = 0
#     class_avg = sum(i[1:]) / i[0]
#     for score in i[1:]:
#         if score > class_avg:
#             cnt += 1
#         else:
#             pass
#     result_list.append('%.3f%%' % (cnt/i[0]*100.0))

# for i in result_list:
#     print(i)

################################################

# def nToSum(a):
#     result = 0
#     for i in a:
#         result += i
#     return result

################################################
# c = input()
# print(ord(c))

################################################
# N = input()
# p = list(map(int,input()))
# print(sum(p))

################################################
# result_list = []
# S = list(input())
# for i in range(97, 123):
#     if chr(i) in S:
#         result_list.append(S.index(chr(i)))
#     else:
#         result_list.append(-1)

# for i in result_list:
#     print(i, end = ' ')

################################################
# T = int(input())
# input_list = []

# for i in range(T):
#     input_list.append(input())

# for i in input_list:
#     for j in i[2:]:
#         print(j * int(i[0]), end = '')
#     print()

# 미해결..
################################################
# S = input()
# S = S.lower()
# cnt_list = []

# if len(S) == 1:
#     print(S[0].upper())
# else:
#     for i in list(set(S)):
#         cnt = 0
#         if S.count(i) == 1:
#             cnt = 0
#         else:
#             cnt = 1
#         cnt_list.append(cnt)
#     if cnt_list.count(1) == 1:
#         print(S[cnt_list.index(1)].upper())
#     else:
#         print('?')

################################################
# print(len(input().strip().split()))

################################################
# a, b = input().split()
# new_a = int(''.join(reversed(a)))
# new_b = int(''.join(reversed(b)))

# if new_a > new_b:
#     print(new_a)
# else:
#     print(new_b)

################################################
# phone = {'A' : 2, 'B' : 2, 'C' : 2,
#         'D' : 3, 'E' : 3, 'F' : 3,
#         'G' : 4, 'H' : 4, 'I' : 4,
#         'J' : 5, 'K' : 5, 'L' : 5,
#         'M' : 6, 'N' : 6, 'O' : 6,
#         'P' : 7, 'Q' : 7, 'R' : 7, 'S' : 7,
#         'T' : 8, 'U' : 8, 'V' : 8,
#         'W' : 9, 'X' : 9, 'Y' : 9, 'Z' : 9,}
# time = [0,2,3,4,5,6,7,8,9,10,11]
# result = 0

# s = input()
# for i in s:
#     result += time[phone.get(i)]
# print(result)

################################################
# s = input()
# croartia_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in croartia_alpha:
#     if i in s:
#         s = s.replace(i,'*')
# print(len(s))

################################################
# n = int(input())
# for w in range(n):
#     word = input().rstrip()
#     for i in range(len(word) - 1):
#         if word[i] != word[i+1]:
#             if word[i] in word[i+1:]:
#                 n -= 1
#                 break
                
# print(n)

################################################
# A, B, C = map(int, input().split())
# if B > C:
#     print(-1)
# elif B - C == 0:
#     print(-1)
# else:
#     print(A // (C - B) + 1)

################################################
# n = int(input())

# start = 1
# cnt = 1

# while n > start:
#     start += 6 * cnt
#     cnt += 1
# print(cnt)

################################################
# import math
# A, B, V = map(int, input().split())
# answer = math.ceil((V - B) / (A - B))
# print(answer)

################################################
# import math

# def solution(p):
#     h, w, n = p
#     answer = ''
#     floor = n % h
#     num = n // h + 1
    
#     if floor == 0:
#         floor = h
#         num -= 1
#     return (floor * 100 + num)

# t = int(input())
# p_list = []
# for _ in range(t):
#     p = list(map(int, input().split()))
#     p_list.append(p)

# for i in p_list:
#     print(solution(i))

################################################
# for _ in range(int(input())):
#     floor = int(input())
#     num = int(input())
    
#     f0 = [x for x in range(1, num+1)]
#     for i in range(floor):
#         for j in range(1, num):
#             f0[j] += f0[j - 1]
#     print(f0[-1])

################################################
# def solution(n):
#     bag = 0
#     while n >= 0:
#         if n % 5 == 0:
#             bag += (n // 5)
#             return bag
#         n -= 3
#         bag += 1
#     return -1

# n = int(input())
# print(solution(n))

################################################
# a, b = map(int, input().split())
# print(a + b)

################################################
# from itertools import permutations as pm

# n, m = map(int, input().split())
# card_list = list(map(int, input().split()))
# card_cb = []
# card_cb = list(pm(card_list, 3))

# cnt = 0
# answer_list = []
# for cards in card_cb:
#     if sum(cards) <= m:
#         answer_list.append(sum(cards))
# print(max(answer_list))

################################################
# N = int(input())
# temp = 0
# for n in range(N):
#     temp = n + sum(map(int, str(n)))
#     if temp == N:
#         print(n)
#         break
# else:
#     print(0)

################################################
# n = int(input())
# peoples = []
# for _ in range(n):
#     peoples.append(list(map(int, input().split())))

# result = []    
# for people in peoples:
#     x, y = people
#     cnt = 1
#     for i in range(n):
#         if x < peoples[i][0] and y < peoples[i][1]:
#             cnt += 1
#     result.append(cnt)

# for i in result:
#     if i == len(result):
#         print(i)
#     else:
#         print(i, end = ' ')

################################################
n = int(input())

num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
        num += 1
        if cnt == n:
            print(num - 1)
            break
    else:
        num += 1