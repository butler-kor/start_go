
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