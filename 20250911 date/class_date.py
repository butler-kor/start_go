from datetime import date

class date_calculator():
    def date_calculator_year_month_day(self,year,month,day):
        data_month = [31,28,31,30,31,30,31,31,30,31,30,31]
        data_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        date_year = year
        date_month = month
        date_day = day
        num1 = 0
        num2 = 0
        if date_year % 4  == 0:
            data_month[1] = 29
            if date_year > 1581 and date_year % 100 == 0:
                data_month[1] = 28
                if date_year % 400 == 0 and date_year % 4 == 0:
                    data_month[1] = 29

        while num1 < date_year :
            if num1 % 4 == 0:
               num2 += 1
            num1 = num1 + 1
        week = ((year * 365) + num2) % len(data_week)
        week_name = data_week[week]
        input_date = date(date_year, date_month, date_day)
        today = date.today()
        delta = today - input_date
        return delta.days,week_name
