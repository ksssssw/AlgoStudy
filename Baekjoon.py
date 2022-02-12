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
# n = int(input())

# num = 666
# cnt = 0
# while True:
#     if '666' in str(num):
#         cnt += 1
#         num += 1
#         if cnt == n:
#             print(num - 1)
#             break
#     else:
#         num += 1

################################################
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))

# nums = list(set(nums))
# nums = sorted(nums)

# for i in nums:
#     print(i)

################################################
# 산술평균
# def average(nums):
#     return round(sum(nums) / len(nums))

# # 중앙값
# def middleNum(nums):
#     nums = sorted(nums)
#     return nums[len(nums) // 2]

# # 최빈값
# from collections import Counter
# def manyNum(nums):
#     nums = sorted(nums)
#     nums_s = Counter(nums).most_common()

#     if len(nums_s) > 1:
#         if nums_s[0][1] == nums_s[1][1]:
#             return nums_s[1][0]
#         else:
#             return nums_s[0][0]
#     else:
#         return nums_s[0][0]


# # 범위
# def rangeNums(nums):
#     nums = sorted(nums)
#     return nums[-1] - nums[0]


# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
    
# print(average(nums))
# print(middleNum(nums))
# print(manyNum(nums))
# print(rangeNums(nums))

################################################
# n = list(str(input()))
# n.sort(reverse=True)
# print("".join(n))

################################################
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(list(map(int, input().split())))
# nums.sort()

# for n in nums:
#     print('{} {}'.format(n[0], n[1]))

################################################
# import sys
# strList = []

# for i in range(int(input())):
#     strList.append(sys.stdin.readline().rstrip())

# strList = list(set(strList))
# strList.sort()
# strList.sort(key = len)
# print('\n'.join(strList))

################################################
# import sys
# peoples = []

# for i in range(int(input())):
#     peoples.append(list(map(str, sys.stdin.readline().rstrip().split())))
# peoples.sort(key = lambda x:(x[0]))

# for i in peoples:
#     print('{} {}'.format(i[0], i[1]))

################################################
# n = int(input())
# nums = list(map(int, input().split()))

# newNums = list(sorted(set(nums)))
# newNums = {newNums[i] : i for i in range(len(newNums))}
# print(*list(newNums[i] for i in nums))

################################################
# n, m = map(int, input().split())
# s = []

# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
    
#     for i in range(1, n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()

# dfs()

################################################
# n, m = map(int, input().split())
# s = []
# t = []

# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str, s)))
        
#     for i in range(start, n+1):
#         if i not in s:
#             s.append(i)
#             dfs(i + 1)
#             s.pop()
# dfs(1)

################################################
# n, m = map(int, input().split())
# s = []

# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return 
        
#     for i in range(1, n+1):
#         s.append(i)
#         dfs()
#         s.pop()
        
# dfs()

################################################
# n, m = map(int, input().split())
# s = []

# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return

#     for i in range(start, n+1):
#         s.append(i)
#         dfs(i)
#         s.pop()
        
# dfs(1)

########### dfs, bfs 공부... ############
# 스택은 후입선출 방식
# 파이썬은 append함수와 pop함수를 사용해서 스택을 구현할 수 있다.
# 따로 함수를 구현할 필요가 없음 두 함수 모두 시간복잡도가 상수임 O(1)
# 거꾸로 출력할때는 print(list_name[::-1])을 통해 거꾸로 출력해주면 됨

# 큐는 선입선출 방식
# 'from collections import deque' 라이브러리를 사용해 가능
# list를 사용하면 시간복잡도가 너무 늘어남
# from collections import deque
# queue = deque()
# queue.append(5) # 삽입
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft() # 가장 왼쪽 데이터를 삭제

# 재귀 함수는 자기 자신을 다시 호출하는 함수를 말한다.
# dfs를 구현할때 자주 사용됨 매우 중요함!!
# Recursive Function == 재귀 함수
# 종료 조건을 잘 넣어줘야함
# def gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)
        
# print(gcd(192, 162))
# 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간단하게 작성할 수 있지만 다른사람이 이해하기 어려울 수 있음

# DFS(Depth - First - Search) - 깊이 우선 탐색
# 스택자료구조 또는 재귀함수를 사용
##### dfs 구현 #####
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = ' ')
    
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]]
# visited = [False] * 9
# dfs(graph, 1, visited)

# BFS는 너비우선 탐색
##### bfs 샘플 #####
# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
    
#     while queue:
#         v = queue.popleft()
#         print(v, end = ' ')
        
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]]
# visited = [False] * 9
# bfs(graph, 1, visited)

##############################################
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
    
#     # 현재 노드를 아직 방문하지 않았다면...
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상하좌우의 위치들도 모두 재귀적으로 호출
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
            
# print(result)
#----------------------------------------------#
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False

#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#     return False

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
    
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1

# print(result)

## 미로탈출문제... 
# from collections import deque

# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
    
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 4방향으로 탐색
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[n - 1][m - 1]

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# print(bfs(0, 0))

################################################
def solution(N):
    temp = str(bin(N)[2:])
    sizeList = temp.split('1')
    print(temp)
    if temp.count('1') > 1:
        return len(max(sizeList))
    else:
        return 0
    
print(solution(51712))