month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day = ("월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일")
HollyDay = {"신정": ["01월 01일"], "구정": ["01월 28일부터 01월 30일까지"], "삼일절": ["03월 01일"], "노동절": ["05월 01일"],
            "근로자의날": ["05월 01일"], "어린이날": ["05월 05일"], "현충일": ["06월 06일"], "광복절": ["08월 15일"], "개천절": ["10월 03일"],
            "추석": ["10월 05일 부터 10월 07일까지"], "한글날": ["10월 09일"], "크리스마스": ["12월 25일"]}
InputMonth = int(input("월을 입력하세요:"))
InputDay = int(input("일을 입력하세요:"))
num1 = 0
num2 = 0
while num1 < InputMonth - 1:
    num2 += month[num1]
    num1 = num1 + 1
num2 = num2 + InputDay
num1 = int((num2 % 7) + 1)
if num1 == 7:
    num1 = 0
print(num2)
print(day[num1])
Question1 = input("공휴일을 찾아 보시겠습니까? Y(1번) , N(2번)")
if Question1 == "Y" or Question1 == "y" or Question1 == "1":
    InputHollyDay = input("공휴일명을 입력하세요 (예) 구정 , 신정 , 크리스마스 등 :   ")
    if InputHollyDay in HollyDay:
        OutputHollyDay = HollyDay.get(InputHollyDay)
        print(f"선택하신 {InputHollyDay}는(은) {OutputHollyDay}입니다.")
else:
    print("프로그램을 종료합니다.")
    exit()
    
    
    #주석 달아서 다르게 보이기