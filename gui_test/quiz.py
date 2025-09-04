# # 퀴즈를 입력하고
# # 답을 입력하고 (4지선다)
# # 정답이면 링크로 연결된 곳에서 정답이라고 뜨고 다른 문제가 등장
# # 오답이면 다른 사이트로 이동하고 오답이라고 뜸
#
# # 1. 퀴즈를 답고 있는 무언가(변수)
# #
# # 2. 정답을 답고 있을 무언가(변수)
# #
# # -------------------------------------------------------
#
# # 문제 출제기능
# #
# # 3. 정답인지 / 오답인지 판단 기능   def 라고 할 수 있다.
# #
# # 4. 사이트로 이동하는 기능         def 라고 할 수 있다.
#
# import random
# import webbrowser
# from operator import truediv
#
# import answer as an
#
# def quiz():
#     pb =random.choice(list(an.quiz.keys()))
#     global  answer = an.quiz[pb]
#     return pb,answer
#     # print(pb)
#     # print(answer)
# # print(quiz())
#
# def goto_url(url):
#     webbrowser.open(url)
#
# def check_answer(correct_answer, user_answer):
#     if correct_answer == user_answer:
#         goto_url("www.naver.com")
#         return True
#     else:
#         goto_url("www.youtube.com")
#         return False
# def wrong_answer():
#     wa = []
#     wa2= []
#     str1 = ""
#     num1 = 0
#     for i in range(3):
#        wa[i] = random.choice(an.wrong)
#     wa.append(answer)
#     while num1 < len(wa):
#         str1 = random.randint(wa)
#         if str1 not in wa2 :
#             wa2.append(str1)
#             num1 = num1 + 1
#
#
#     return wa

import random
import webbrowser
import answer as an

answer = None

def quiz():
    global answer
    pb = random.choice(list(an.quiz.keys()))
    answer = an.quiz[pb]
    return pb, answer

def goto_url(url):
    webbrowser.open(url)

def check_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        goto_url("https://www.youtube.com/shorts/BVJUrZSgplg")
        return True
    else:
        goto_url("https://www.youtube.com/watch?v=ok03kNfAYB8")
        return False

def wrong_answer():
    wa = []
    while len(wa) < 3:
        choice = random.choice(an.wrong)
        if choice not in wa:
            wa.append(choice)
    return wa
