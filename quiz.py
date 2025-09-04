# 퀴즈를 보여주고
#답을 입력한다.

import sys
import answer as an
import random
import webbrowser

def quiz():
    pb =random.choice(list(an.quiz.keys()))
    # print(pb)
    answer = an.quiz[pb]
    # print(answer)
    return pb,answer

print(quiz())

quiz()

def check_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        return True
    else:
        return False


def goto_url(url):
    webbrowser.open(url)