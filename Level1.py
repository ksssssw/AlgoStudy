######################################
#           로또 맞추기                 #
######################################
# def solution(lottos, win_nums):
#     answer = []
#     lottos_rank = [6, 6, 5, 4, 3, 2, 1]
#     cnt = 0
#     zero_cnt = 0

#     for n in lottos:
#         if n in win_nums:
#             cnt += 1
#         if n == 0:
#             zero_cnt += 1

#     answer.append(lottos_rank[zero_cnt + cnt])
#     answer.append(lottos_rank[cnt])

#     return answer


# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

# print(solution(lottos, win_nums))


######################################
#           신규 아이디 추천             #
######################################
# def solution(new_id):
#     answer = ""

#     # step 1
#     new_id = new_id.lower()

#     # step 2
#     character = "~!@#$%^&*()=+[{]}:?,<>/"
#     new_id = "".join(x for x in new_id if x not in character)

#     # step 3
#     character = ".."
#     while character in new_id:
#         new_id = new_id.replace(character, ".")

#     # step 4
#     if new_id[0] == ".":
#         new_id = new_id[1:]
#     if len(new_id) == 0:
#         pass
#     elif new_id[-1] == ".":
#         new_id = new_id[:-1]

#     # step 5
#     if len(new_id) == 0:
#         new_id += "a"

#     # step 6
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#         if new_id[-1] == ".":
#             new_id = new_id[:-1]

#     # step 7
#     if len(new_id) <= 2:
#         while len(new_id) < 3:
#             new_id += new_id[-1]

#     return new_id


# new_id = "=.="
# print(solution(new_id))

######################################
#          숫자 문자열과 영단어           #
######################################
# def solution(s):
#     numbers = [
#         "zero",
#         "one",
#         "two",
#         "three",
#         "four",
#         "five",
#         "six",
#         "seven",
#         "eight",
#         "nine",
#     ]
#     for num in numbers:
#         if num in s:
#             s = s.replace(num, str(numbers.index(num)))
#     return int(s)


# s = "one4seveneight"
# print(solution(s))

######################################
#            키패드 누르기              #
######################################
# import math


# def solution(numbers, hand):
#     answer = ""
#     key_pad = {
#         1: [0, 0],
#         2: [0, 1],
#         3: [0, 2],
#         4: [1, 0],
#         5: [1, 1],
#         6: [1, 2],
#         7: [2, 0],
#         8: [2, 1],
#         9: [2, 2],
#         "*": [3, 0],
#         0: [3, 1],
#         "#": [3, 2],
#     }
#     l_hand = key_pad["*"]
#     r_hand = key_pad["#"]

#     for num in numbers:
#         if num in [1, 4, 7]:
#             answer += "L"
#             l_hand = key_pad[num]
#         elif num in [3, 6, 9]:
#             answer += "R"
#             r_hand = key_pad[num]
#         else:
#             l_dist = math.ceil(
#                 abs(
#                     math.sqrt(
#                         pow(key_pad[num][0] - l_hand[0], 2)
#                         + pow(key_pad[num][1] - l_hand[1], 2)
#                     )
#                 )
#             )
#             r_dist = math.ceil(
#                 abs(
#                     math.sqrt(
#                         pow(key_pad[num][0] - r_hand[0], 2)
#                         + pow(key_pad[num][1] - r_hand[1], 2)
#                     )
#                 )
#             )
#             if l_dist > r_dist:
#                 answer += "R"
#                 r_hand = key_pad[num]
#             elif l_dist < r_dist:
#                 answer += "L"
#                 l_hand = key_pad[num]
#             elif l_dist == r_dist:
#                 if hand == "left":
#                     answer += "L"
#                     l_hand = key_pad[num]
#                 else:
#                     answer += "R"
#                     r_hand = key_pad[num]

#     return answer


# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# print(solution(numbers, hand))

######################################
#           없는 숫자 더하기             #
######################################
# def solution(numbers):
#     answer = 0
#     for i in range(1, 10):
#         if i not in numbers:
#             answer += i
#     return answer


# numbers = [1, 2, 3, 4, 6, 7, 8, 0]
# print(solution(numbers))

######################################
#               음양 더하기             #
######################################
# def solution(absolutes, signs):
#     answer = 0
#     for i, j in zip(absolutes, signs):
#         if j == True:
#             answer += i
#         else:
#             answer -= i
#     return answer


# absolutes = [4, 7, 12]
# signs = [true, false, true]
# print(solution(absolutes, signs))

######################################
#                 내적                #
######################################
# def solution(a, b):
#     answer = 0
#     for i, j in zip(a, b):
#         answer += i * j
#     return answer


# a = [1, 2, 3, 4]
# b = [-3, -1, 0, 2]
# print(solution(a, b))

######################################
#        완주하지 못한 선수              #
######################################
# def solution(participant, completion):
#     answer = ""
#     participant.sort()
#     completion.sort()

#     for p, c in zip(participant, completion):
#         if p != c:
#             return p

#     return participant.pop()


# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# print(solution(participant, completion))

######################################
#               K번째수               #
######################################
# def solution(array, commands):
#     answer = []
#     arr = []
#     for i in commands:
#         arr = array[i[0] - 1 : i[1]]
#         arr.sort()
#         answer.append(arr[i[2] - 1])
#     return answer


# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))

######################################
#               모의고사               #
######################################
# def solution(answers):
#     result = []
#     no_1 = [1, 2, 3, 4, 5]
#     no_2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     no_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     scores = [0, 0, 0]

#     for idx, ans in enumerate(answers):
#         if ans == no_1[idx % len(no_1)]:
#             scores[0] += 1
#         if ans == no_2[idx % len(no_2)]:
#             scores[1] += 1
#         if ans == no_3[idx % len(no_3)]:
#             scores[2] += 1

#     for person, score in enumerate(scores):
#         if score == max(scores):
#             result.append(person + 1)

#     return result


# answers = [1, 3, 2, 4, 2]
# print(solution(answers))

######################################
#                체육복                #
######################################
# def solution(n, lost, reserve):
#     answer = 0
#     c = 0

#     lost_n = list(set(lost) - set(reserve))
#     reserve_n = list(set(reserve) - set(lost))

#     for l in lost_n:
#         if l - 1 in reserve_n:
#             c += 1
#             reserve_n.remove(l - 1)
#         elif l + 1 in reserve_n:
#             c += 1
#             reserve_n.remove(l + 1)

#     answer = n - (len(lost_n) - c)

#     return answer


# n = 5
# lost = [2, 4]
# reserve = [2, 3]
# print(solution(n, lost, reserve))

######################################
#                폰켓몬                #
######################################
# import itertools

# def solution(nums):
#     lengths = len(nums) // 2
#     u_type = list(set(nums))
#     answer = 0
    
#     for i in u_type:
#         if answer < lengths:
#             answer += 1
    
#     return answer


# nums = [3,3,3,2,2,4]
# print(solution(nums))

######################################
#                실패율                #
######################################
# def solution(N, stages):
#     answer = []
#     result = {}
#     total_player = len(stages)
    
#     for i in range(1, N + 1):
#         if total_player != 0 :
#             cnt = stages.count(i)
#             temp = cnt / total_player
#             result[i] = temp
#             total_player -= cnt
#         else:
#             result[i] = 0
#     # print(result)
#     # sort_result = dict(sorted(result.items(), key = lambda item : item[1], reverse = True))
#     # answer = list(sort_result.keys())
    
#     return sorted(result, key = lambda x : result[x], reverse = True)

# N = 4
# # stages = [2, 1, 2, 6, 2, 4, 3, 3]
# stages = [4,4,4,4,4]
# print(solution(N, stages))

######################################
#           약수의 개수와 덧셈           #
######################################
# def checkNumber(num):
#     cnt = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cnt += 1
#     if cnt % 2 == 0:
#         return True
#     else:
#         return False

# def solution(left, right):
#     answer = 0
#     for i in range(left, right + 1):
#         if checkNumber(i) == True:
#             answer += i
#         else:
#             answer -= i
#     return answer


# left = 13
# right = 17
# print(solution(left, right))

######################################
#               3진법 뒤집기            #
######################################
# def solution(n):
#     answer = ''
    
#     while n >= 1:
#         n, rest = divmod(n, 3)
#         answer += str(rest)
    
#     answer = int(answer, 3)
    
#     return answer

# n = 45
# print(solution(n))

######################################
#                예산                 #
######################################
def solution(d, budget):
    answer = 0
    d = sorted(d)
    rest = budget
    
    for cost in d:
        if cost < rest:
            answer += 1
            rest -= cost
    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))