# 선생님이 만든 코드 멜론 최신곡 50곡의 순위 제목 가수 앨범명 선택 출력이 가능한 코드
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# Headers = {'User-Agent' : 'Mozilla/5.0 (Window NT 10.0 : Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) chrome / 128.0.0.0 Sarari/537.36'}
# Url = "https://www.melon.com/new/index.htm"
# Req = requests.get(Url,headers = Headers)
# Html = Req.text
# Soup = BeautifulSoup(Html,'html.parser')
# NewList50 = Soup.select('tbody tr')
# data_list = []
#
# for Memo in NewList50:
#     temp = []
#     Rank = Memo.select_one('td div span.rank').get_text()
#     Title = Memo.select_one('td div div  div.ellipsis.rank01  span  a').get_text()
#     Artist = Memo.select_one('td div div div.ellipsis.rank02  a').get_text()
#     Album = Memo.select_one('td div div div.ellipsis.rank03  a').get_text()
#
#     temp.append(Rank)
#     temp.append(Title)
#     temp.append(Artist)
#     temp.append(Album)
#
#     data_list.append(temp)
#
#
#
# columns = ['순위','제목','가수','앨범']
# df_list = pd.DataFrame(data_list, columns=columns)
# address = r'D:\파이썬 수업\git\pythonstart'
# df_list.to_excel(excel_writer = address+r'\melon.xlsx')


# 새로운 크롤링 연습
# 1. <body> 태그 안에 <div> 태그가 두개 포함  <body> 태그의 내용을 추출
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # 1번 예제
# html_doc ="""
# <!doctype html>
# <html>
#     <head>
#         기초 웹 크롤링 따라하기
#     </head>
#     <body>
#         <div>첫 번재 부분</div>
#         <div>두 번째 부분</div>
#     </body>
# </html>
# """
# bs_obj = BeautifulSoup(html_doc,"html.parser")
# body = bs_obj.find("body")
# print(body)
#
# # 1번 만약 <div> 태그의 내용만 불러오고 싶다면 find 메서드에 div 를 입력하면 된다.
# body= bs_obj.find("div")
# print(body)
#
# # 2번 <div> 가 2개 이므로 2개의 내용을 모두 불러오고 싶다면 find 메서드를 find_all 메서드로 바꾸면 된다.
# body= bs_obj.find_all("div") # div 태그의 내용이 2개 이상으므로 리스트로 작성되어 나온다. 결과값)[<div>첫 번재 부분</div>, <div>두 번째 부분</div>]
# print(body)# 이때 나온 <div>첫 번재 부분</div> 는 body[0]번째 태그 내용이고 <div>두 번째 부분</div>]은 body[1]번째 내용이다.
# # 리스트 자료형이기 때문에 인덱스를 이용하여 요소에 접근할 수 있다.
#
# # 3번 리스트 body의 2번째 요소만 가져오고 싶을 때
# div2 = body[1] # 인덱스를 이용하여 2분째 요소만 div2에 반환한다.
# print(div2)
#
# # 4번 위 코드처럼 출력하면 텍스트와 태그가 같이 출력하게 된다. 텍스트만 출력하는 코드
# div2 = body[1]
# print(div2.text) # .text를 붙여서 태그가 아닌 텍스트만 출력하게 한다.  출력문) 두 번째 부분


# 2번 예제

# html_doc ="""
# <!doctype html>
# <html>
#     <head>
#         <title> 기초 웹 크롤링 </title>
#     </head>
#         <body>
#             <table border ="1">
#                 <caption> 과일가격 </caption>
#                 <tr>
#                     <th>상품</th>
#                     <th>가격</th>
#                 </tr>
#                 <tr>
#                     <td> 오렌지 </td>
#                     <td> 100 </td>
#                 </tr>
#                 <tr>
#                     <td> 사과 </td>
#                     <td> 150 </td>
#                 </tr>
#             </table>
#             <table border ="2">
#                 <caption> 의류가격 </caption>
#                 <tr>
#                     <td> 상품 </td>
#                     <td> 가격 </td>
#                 </tr>
#                 <tr>
#                     <td> 셔츠 </td>
#                     <td> 3000 </td>
#                 </tr>
#                 <tr>
#                     <td> 바지 </td>
#                     <td> 5000</td>
#                 </tr>
#             </table>
#         </body>
#     </html>
# """
#
# # 5번 태그의 속성을 이용해 html 문서를 검색 내용추출
# bs_obj = BeautifulSoup(html_doc , "html.parser")
# clothes = bs_obj.find_all("table",{"border" : "2"})
# print(clothes)  #<table border="2">의 내용만 출력




# 20250627 예스24 1위부터 10위까지 크롤링
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# Headers = {'User-Agent' : 'Mozilla/5.0 (Window NT 10.0 : Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) chrome / 128.0.0.0 Sarari/537.36'}
# url ='https://www.yes24.com/main/default.aspx'
# res = requests.get(url)
# # print(res) # Response[200] 이 뜨면 정상
# soup = BeautifulSoup(res.text,'html.parser')
#
# books = soup.select('li.tp02')
# # print(books)
# booklist = []
#
# for book in books :
#     rank = book.select('strong')[0].text
#     title = book.select('strong')[1].text
#     author = book.select('em')[1].text
#     url = 'https://www.yes24.com' + book.select_one('a')['href']
#     booklist.append([rank, title, author, url])
#     print(rank,title,author,url)
#
# df = pd.DataFrame(booklist,columns=['순위','제목','저자','링크'])
# df.to_excel('D:\파이썬 수업\git\pythonstart\yes24best10.xlsx', index=False)



#250701 뮤비차트 1위부터 20위  순위 / 제목 / 링크주소크롤링

# import requests
# from bs4 import BeautifulSoup  # BeautifulSoup import
#
# response = requests.get('https://m.moviechart.co.kr/rank/realtime/index/image')
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
# ranking = 1
# for b in soup.select("ul[class=movieBox-list] li[class=movieBox-item]"):
#     score = b.select('a p')[0]
#     tag = b.select('a')[0]
#     attr = tag.get('href')
#     name=b.select('div[class=movie-title] h3')[0]
#     print("순위: " + score.text + ", 제목: " + name.text + ", 주소: " + attr)



# 250710 수업 선생님 코드 (교육용 기록)
# import requests
# from bottleneck import rankdata
# from bs4 import BeautifulSoup  # BeautifulSoup import
# from pyparsing import nullDebugAction
#
# response = requests.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1')
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
# tit_category = ""
# book_name = ""
# auth = ""
# company = ""
# date = ""
# for b in soup.select("div[class=ss_book_box]"):
#     rank = b.select_one("table table div").text
#     for i, info in enumerate(b.select("td > div > ul")):
#         if i % 2 == 1:
#             continue
#         sub_info = info.select("li")
#
#         for j in sub_info:
#             if "tit_category" in str(j):
#                 tit_category = j.select_one("span[class=tit_category]").text
#                 book_name = j.select_one("li > a[class=bo3]").text
#             if "Author" in str(j):
#                 p = j.text
#                 auth = p.split(sep = '|')[0].strip()
#                 company = p.split(sep='|')[1].strip()
#                 date = p.split(sep='|')[2].strip()
#
#     print("순위: " + rank + "국내/해외: " + tit_category + "제목: " + book_name + "작가: " + auth + "출판사: " + company + "날짜: " + date)



import requests
from bottleneck import rankdata
from bs4 import BeautifulSoup  # BeautifulSoup import
from pyparsing import nullDebugAction

response = requests.get('https://music.bugs.co.kr/chart')
html = response.text
soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
albumname = ""
artist = ""
title = ""

for b in soup.select("tbody  tr"):
    rank = b.select_one("div[class] > strong").text
    print(rank + "위")
    for i, info in enumerate(b.select_one("tr td")) :
        if i % 2 == 1:
            continue
        sub_info = info.select