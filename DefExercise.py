#def 함수를 사용하여 구구단 만들기
from win32process import LIST_MODULES_32BIT
from zstandard.backend_cffi import STRATEGY_BTLAZY2


# def gugudan(x,y):
#     result = x * y
#     return result
#
# num1 = int(input("첫번째 숫자를 입력하세요:"))
# num2 = int(input("두번째 숫자를 입력하세요:"))
#
# print(f"{num1} X {num2} = ",(gugudan(num1,num2)),"입니다.")

# def 함수에 슬라이싱을 사용하여 문자열을 더하고 역순으로 출력
# def Reverse(Str1, Str2):
#     Str3 = Str1 + Str2
#     return Str3[ : : -1]
#
# str1 = input("첫번째 하고 싶은 말을 적으세요:")
# str2 = input("두번째 하고 싶은 말을 적으세요:")
# print(Reverse(str1,str2))

#def를 이용하여 성적리스트를 받고 평균 값을 출력
# def Score(no1,no2,no3):
#    result1 = sum(no1) / len(no1)
#    result2 = sum(no2) / len(no2)
#    result3 = sum(no3) / len(no3)
#    return result1,result2,result3
#
# List1 = ['수학','영어','과학','물리']
# List2 = []
# num1 = 0
# num2 = 0
# num3 = 0
# no1Student = []
# no2Student = []
# no3Student = []
# for i in range(1,4):
#     num2 = num2 + 1
#     List2 = []
#     print(f"{num2}번째 학생의 점수를 입력해 주세요")
#     num3 = 0
#     for j in range(len(List1)):
#         num1 = int(input(f"{num2}번째 학생의 {List1[num3]} 점수를 입력해주세요:"))
#         List2.append(num1)
#         num3 = num3 + 1
#     if num2 == 1:
#         no1Student.extend(List2)
#     elif num2 == 2 :
#         no2Student.extend(List2)
#     elif num2 == 3 :
#         no3Student.extend(List2)
# print(no1Student)
# print(no2Student)
# print(no3Student)
#
# result = Score(no1Student,no2Student,no3Student)
#
# print(f"1번째 학생의 평균 값은 {result[0]} 입니다.")
# print(f"2번째 학생의 평균 값은 {result[1]} 입니다.")
# print(f"3번째 학생의 평균 값은 {result[2]} 입니다.")

# 250524 def 연습 기본계산기
# def Calculator(FirstNum,Choice,SecondNum):
#    def add(FN,SN):
#        return FN + SN
#
#    def sub(FN,SN):
#        return FN - SN
#
#    def mul(FN,SN):
#        return FN * SN
#
#    def div(FN,SN):
#        if FN == 0 and SN == 0:
#            return "0으로는 숫자를 나눌 수가 없습니다."
#        else:
#            return FN / SN
#    def power(FN,SN):
#         return FN ** SN
#
#    if Choice == 1:
#        return add(FirstNum,SecondNum)
#
#    elif Choice == 2 :
#        return sub(FirstNum,SecondNum)
#
#    elif Choice == 3:
#        return mul(FirstNum, SecondNum)
#
#    elif Choice == 4:
#        return div(FirstNum, SecondNum)
#
#    elif Choice == 5:
#        return power(FirstNum, SecondNum)
#
#    else:
#        return "잘못된 선택입니다."
#
#
#
# FirstNum = int(input("첫번째 숫자를 입력하세요:"))
# while True:
#     Choice = input("수식을 입력하세요 : 1) 더하기 , 2)빼기 , 3)곱하기 , 4)나누기, 5)거듭제곱 :")
#     SecondNum = int(input("두번째 숫자를 입력하세요:"))
#     if Choice == "1" or Choice == "1번" or Choice == "더하기" or Choice == "+":
#         Choice = 1
#
#     elif Choice == "2" or Choice == "2번" or Choice == "빼기" or Choice == "-":
#           Choice = 2
#
#     elif Choice == "3" or Choice == "3번" or Choice == "곱하기" or Choice == "*":
#           Choice = 3
#
#     elif Choice == "4" or Choice == "4번" or Choice == "나누기" or Choice == "/":
#           Choice = 4
#
#     elif Choice == "5" or Choice == "5번" or Choice == "거듭제곱" or Choice == "**":
#           Choice = 5
#
#     LastNum = Calculator(FirstNum,Choice,SecondNum)
#     FirstNum = LastNum
#     print(FirstNum)


# 217번 문제 현재 가격을 입력 받아 상한가(30%)를 출력하는 print_upper_price 함수를 정의하라.
# def print_upper_price(Innum):
#     return Innum * 1.3
#
# num1 = int(input("값을 입력하시오:"))
# Innum = print_upper_price(num1)
# print(Innum)

# 218번 문제 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
# def print_sum(FirstNum,SecondNum):
#     sum = FirstNum + SecondNum
#     return sum
#
# num1 = int(input("첫번째 숫자를 입력하시오:"))
# num2 = int(input("두번째 숫자를 입력하시오:"))
# Result = print_sum(num1,num2)
# print(Result)

#219번 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

# def print_arithmetic_operation(FirstNum,SecondNum):
#     sum = FirstNum + SecondNum
#     sub = FirstNum - SecondNum
#     mul = FirstNum * SecondNum
#     div = FirstNum / SecondNum
#     return sum,sub,mul,div
#
# num1 = int(input("첫번째 숫자를 입력하시오:"))
# num2 = int(input("두번째 숫자를 입력하시오:"))
# Result = print_arithmetic_operation(num1,num2)
# print(Result)


#220번 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

# def print_max(FirstNum,SecondNum,ThirdNum):
#     MaxNum = 0
#     if FirstNum > MaxNum:
#         MaxNum =FirstNum
#     if MaxNum < SecondNum:
#         MaxNum = SecondNum
#     if MaxNum < ThirdNum:
#         MaxNum = ThirdNum
#
#     return MaxNum
#
# First_Num = int(input("첫번째 숫자를 입력하세요:"))
# Second_Num = int(input("두번째 숫자를 입력하세요:"))
# Third_Num = int(input("세번째 숫자를 입력하세요:"))
#
# Max_num = print_max(First_Num,Second_Num,Third_Num)
# print(Max_num)

# 221번 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# def print_reverse(string):
#     print(string[ : : -1])
#
# print_reverse("python")


# 222번 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# def print_score(FirstNom, SecondNum, ThirdNum):
#     return (FirstNom + SecondNum + ThirdNum) / 3
#
# result = print_score(1,2,3)
# print(result)

# or

# def print_score(ScoreList):
#     return(sum(ScoreList)/len(ScoreList))
#
# result = print_score([1,2,3])
# print(result)

#223번 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# def print_even(List):
#     for i in List:
#         if i % 2 == 0:
#             print(i)
#
# print_even([1, 3, 2, 10, 12, 11, 15])

# 224번 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

# def print_key(dic):
#     for i in dic.keys(): # value 만 출력할 때는 keys 대신 values 를 넣으면 된다.
#         print (i)
#
# print_key({"이름":"김말똥", "나이":30, "성별":0})


#225 my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# def print_value_by_key  (my_dict, key):
#     print(my_dict[key])
#
# my_dict = {"10/26": [100, 130, 100, 100], "10/27": [10, 12, 10, 11]}
# print_value_by_key  (my_dict, "10/26")

#226번 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

# def print_5xn(Str):
#     print(Str[:5:])
#     print(Str[5: : ])
#
# print_5xn("아이엠어보이유알어걸")

#227번 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.

# def print_mxn(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num + 1) :
#         print(line[x * num: x * num + num])
#
# print_mxn("아이엠어보이유알어걸", 3)


# 228번 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

# def calc_monthly_salary(x):
#     print(int(x / 12))
#
#
# calc_monthly_salary(12000000)


# 229번 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)

# 왼쪽 100
# 오른쪽 200


# 230번 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)

# 욎쪽 200
#오른쪽 100

# 231번 아래 코드를 실행한 결과를 예상하라.

# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)

# 틀렸음   정답 : 에러가 발생한다. 함수 안에서 계산된 것은 함수 밖에서는 접근이 불가능하다 마지막에 리턴이 필요함


# 232번 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.

# def make_url(urladdress):
#     url = "www." + urladdress + ".com"
#     return(url)
#
# print(make_url("naver"))


#223번 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

# def print_even(List):
#     List1 = []
#     for i in List:
#         if i % 2 == 0 :
#             List1.append(i)
#     return List1
#
# print(print_even([1, 3, 2, 10, 12, 11, 15]))


# 224번 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

# def print_keys(keys):
#     for key in keys.keys():
#         print(key)
#
#
# dic1 =  ({"이름":"김말똥", "나이":30, "성별":0})
# print_keys(dic1)

# 225번 my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다. my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.


# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
#
# def print_value_by_key (my_dict, key) :
#     print(my_dict[key])
#
# print_value_by_key  (my_dict, "10/26")

#233번 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

# def make_list(A):
#     b = []
#     for i in A :
#         b.append(i)
#     print(b)
#
# make_list("abcd")

# 234번 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

# def pickup_even(my_list):
#     num1 = 0
#     List1 = []
#     for i in my_list:
#         if i % 2 == 0:
#             List1.append(i)
#     return (List1)
#
# print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235번 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

# def convert_int(Convert):
#     num1 = ""
#     Con = Convert.split(",")
#     for i in Con:
#         num1 = num1 + i
#     print(int(num1))
#
# convert_int("1,234,567")

#236번 아래 코드의 실행 결과를 예측하라.

# def 함수(num) :
#     return num + 4
#
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)
#
# 예측 : a 에 합수 10이 입력되어 4가 더해져 14가 됨
#       b 에 a 함수값 14와 4가 더해져서 18이 됨
#       c d에 b 함수값 18과 4가 더해져서 22가 됨

#237번 아래 코드의 실행 결과를 예측하라.

# def 함수(num) :
#     return num + 4
#
# c = 함수(함수(함수(10)))
# print(c)
#
#  예측 : 가장 안쪽에 있는 함수가 10이며 10은 num이 된다. 10 + 4 = 14
#         두번째 함수가 14이며 num 은 14가 된다 14 + 4 = 18
#         마지막 함수가 18이며 num은 18이 된다 18 + 4 = 22

#238번 아래 코드의 실행 결과를 예측하라.

# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     return num * 10
#
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 예측 :  a는 함수1에 대입되며 num은 10이 된다 10 + 4 = 14
#        c는  함수2에 대입되며 a의 값은 14이므로 num은 14가 된다. 14 * 10 = 140
#        print(c)는 140을 출력한다.

# 239번 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
#
# c = 함수2(10)
# print(c)
#
# # 예측 : 틀렸음
#          우선 함수2에 10으로 바인딩 num은 10이 됨 10 + 2 = 12
#          함수1을 호출
#          num은 12를 함수1로 보내 num은 12로 바인딩 12 + 4 = 16
#          함수1의 동작이 끝나고 함수2 return으로 돌아옴
#          함수2의 값은 16을 리턴 c는 16이 됨

#240번 아래 코드의 실행 결과를 예측하라.

# def 함수0(num) :
#     return num * 2
#
# def 함수1(num) :
#     return 함수0(num + 2)
#
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
#
# c = 함수2(2)
# print(c)
#
# 예측 : 함수2에 2를 바인딩 num은 2가 됨 2 + 10 = 12
#        함수2는 함수1을 호출 num의 값 12는 함수1에 바인딩 num은 12가 됨 12 + 2 = 14
#        함수1은 함수0을 호출 num의 값 14는 함수0에 바인딩 num은 14가 됨 14 * 2 = 28
#        함수0의 동작이 끝나고 함수2로 돌아옴
#        함수2는 최종 28을 리턴하고 c는 28을 반환받음

#모듈
#241번 datatime모듈을 사용해서 현재 시간 화면에 출력
# import datetime
# NowTime = datetime.datetime.now()
# print(NowTime)

#242번 datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

# import datetime
# NowTime = datetime.datetime.now()
# print(NowTime,type(NowTime))

# 243번 datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

# import datetime
# now = datetime.datetime.now()
# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)
#  # 틀렸음


# # 1부터 100까지 합을 구하는 코드를 def 로 만들기
#
# def add(i):
#     a = 0
#     for k in range(i+1):
#         a += k
#     return a
#
# print(add(100))
#
#
# # 입력한 숫자에서 짝수만 추출하여 모두 더해보자
# def add (i):
#     a = 0
#     for k in range(i + 1):
#         if k % 2 == 0:
#             a += k
#     return a
#
# print(add(100))
#
# # 랜덤한 숫자 를 랜덤개를 만들고 숫자를 하나 받아서 그 숫자보다 작은 숫자를 출력한다.
# import random
# def random1(a,b):
#     num1 = 0
#     num2 = 0
#     List1 = []
#     List2 = []
#     while num1 < a :
#         num2 = random.randint(1,10)
#         if num2 not in List1:
#             List1.append(num2)
#         num1 = num1 + 1
#     num1 = 0
#     while num1 < len(List1):
#         if List1[num1] < b:
#             num2 = List1[num1]
#             List2.append(num2)
#         num1 = num1 + 1
#     return List2
#
# print(random1(10,7))

# 자리수 더하기
# def stradd(i):
#     a = 0
#     b = 0
#     c = str(i)
#     while a < len(c):
#         b += int(c[a])
#         a += 1
#     return b
#
#
# print(stradd('12345'))


# # 팩토리얼
# def add(i):
#     a= 0
#     for k in range(i+1):
#         a += k
#     return a
#
# print(add(100))
#
# # 지수 구하기
# def jisu(a,n):
#     num1 = a
#     num2 = 1
#     for i in range(n):
#         num2 *= a
#     return num2
#
# a = 2
# n = 4
# print(jisu(a,n))

# 약수 구하기
def divisor(FirstNum,SecondNum):
    num1 = 0
    num2 = []
    num3 = []
    if FirstNum < SecondNum :
        num1 = FirstNum
        FirstNum = SecondNum
        SecondNum = num1
    num1 = 1
    while num1 < FirstNum:
        if FirstNum % num1 == 0:
            num2.append(num1)
        if SecondNum % num1 == 0:
            num3.append(num1)
        num1 = num1 + 1
    print(num2)
    print(num3)
num1 = int(input("첫번째 숫자를 입력하세요:"))
num2 = int(input("두번째 숫자를 입력하세요:"))
divisor(num1,num2)

