# HTML과 XML을 분석해주고 다운로드 같은 기능은 urllib로 해야할 것.

# 분석을 html 통체로 가져와서 특정한 것만 가져오라라고 돕는 것.


from bs4 import BeautifulSoup as bea
import pandas as pd
# html="""
# <html><body>
# <h1>스크레핑이란?</h1>
#      <p>웹 페이지를 분석하는 것</p>
#      <p>원하는 부분을 추출하는 것</p>
# </body></html>

# """

# soup=bea(html,"html.parser") # parser 는 \n을 인식해서 \n시키겠다는 의미
# soup=bea(html,'lxml') # lxml도 거의 같음. parser와.

# # print(soup)
# h1=soup.html.body.h1
# text=soup.html.body.p.text
# h1_string=soup.html.body.h1.string
# p_nextsibling=soup.body.p.next_sibling.next_sibling
# print(p_nextsibling)

# -----------------------------------
# html에서 
# get방식 ?...,
# tag, id,
# id 요소로 찾는 방법 : 자주 나오는 요소
# head : 
# id : 손흥민, 사과, 버튼 ... 모두 한개
# class : 축구선수 , 과일 : 사과 ... : 같은 급에 해당하는 여러개를 포함

# head사용 : txt에다가 복사 html확장자
# html="""
# <html>
# <head>이것이 헤드입니다.</head>
# <body>
#      <h1 id="title">id속성이라고해,title이라고하면 h1찾아가기</h1>
#      <p id="boby">웹 페이지를 분석하는 것</p>
#      <p>원하는 부분 추출하는 것</p>
# """

# soup=bea(html,'html.parser')
# f=soup.find(id="title")#아주 자주쓴다. 찾아라 id는 꼭 명시한다.
# j=soup.find(id="body")
# print(f)
#--------------------------------------------


# find보다 자주쓰이는 find_all()
# ul 은 unordeded list , 순서가 없는 리스트. 리스트 안에는 1번2번 3번 여러개가 있음.
# href 는 속성이야.
# a는 Tag의 이름임.
html="""
<html>
<body>
     <ul>
          <li> 리스트 인덱스야
               <a href="https://www.naver.com">
               a태그에서 hyperReference네이버
               </a>
               <a href="https://www.google.com">
               리스트 인덱스는 여기까지야.
               </a>
          </li>
     </ul>
</body>
</html>
"""

# soup=bea(html,"html.parser")

# k=soup.find('a')
# j=soup.find_all('a')
# print(k,j)

# link=soup.find('a')
# print(link.text)

# links=soup.find_all('a')
# for link in links:
#      print(link.attrs['href'])
#      print(link.text)
     
#----------------------------------

#url 과 beauti 로 조져보자.
import urllib.request as req
url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# res=req.urlretrieve(url)
res=req.urlopen(url).read()

# print(res) # 개판임을 알 수 있다.
soup=bea(res,'html.parser')
# print(soup)

i=soup.find("wf")
# print(i.text) # wf는 사전에 사이트에 들가서 html의 구조를 훑었다.

info=soup.find_all('wf') # len= 534->출제자의 의도, wf의 개수는 몇개인가를 구했다.
# print(info)
# times=0
# for i in info:
#      print(i.text)
#      times+=1# 534
# print(times)

#-----------------------------------------

# select 로 하면 다 찾아준다. 
# select all, find_all 둘다 써도 되는 html
html=""" 이렇게 하면 틀리고 h1은 반드시 div에 있어야 아래 코드가 작동
<html>
<body>
<div>
<h1 id="meigen">퀴즈북스 도서</h1>
<ul class="items">
     <li>UnityGame Effect</li>
     <li>Swift</li>
     <li>ModernWebsite</li>
</ul>
</div>
</body>
</html>
"""
html_fix=""" 이렇게 하면 틀리고 h1은 반드시 div에 있어야 아래 코드가 작동
<html>
<body>
<div id="meigen">
<h1>퀴즈북스 도서</h1>
<ul class="items">
     <li>UnityGame Effect</li>
     <li>Swift</li>
     <li>ModernWebsite</li>
</ul>
</div>
<div id="No2">
<h1>퀴즈북스 도서</h1>
<ul class="kkbs">
     <li>UnityGame Effect</li>
     <li>Swift</li>
     <li>ModernWebsite</li>
</ul>
</div>
</body>
</html>
"""

soup=bea(html_fix,'html.parser')

k=soup.select_one("div#meigen >h1").string # CSS SELECTOR : #은 약속. id라는 뜻임. class는 쩜으로\
#string 또는 text
j=soup.select_one("div#meigen") #이것도 되고

i=soup.select_one("#meigen") # 이것도 되고
i=soup.select_one("#meigen>h1") # 이것도 되고

cls=soup.select("div#meigen > ul.items > li")# class는 .으로 아이디를 구별
no2=soup.select("div#No2 > ul.items > li")
# for i in no2:
#      print(i.text)
     
# div안 거치고 그냥 class 이름만 찾아서 가기

cls=soup.select(".kkbs > li") # it made it..
# print(cls)

# find_all로

fia=soup.find_all('div',attrs={'class':'items'}) # 이거 틀림
fia=soup.find_all('ul',attrs={'class':'items'}) # 이거 맞음
# print(fia)
# 가장 자주 쓰는 방법
fia=soup.find_all(class_='items')

# for i in fia:
#      print(i.text)
     
     
# 달라/환율 ---------------------------

import urllib.request as req
from bs4 import BeautifulSoup as bea
# url="https://finance.naver.com/marketindex/"

# u=req.urlopen(url).read()
# soup=bea(u,"html.parser")

# value=soup.select("div#container>div.market_include>div.market_data>div.market1>div.data>ul.data_lst>li.on>a.head.usd")

# value2=soup.select("div#wrap")

# fa=soup.find_all(class_=["h3.h_list","value"])
# print(fa[0].text,fa[1].text)# 현재 환율의 값이 등장해야함


# 네이버 검색해서 ..
from urllib.parse import quote_plus
furl="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
# que=input() # -> 신발
# one=quote_plus(que) # ->%EC%8B%A0%EB%B0%9C
# two=que.encode('utf-8')# ->b'\xec\x8b\xa0\xeb\xb0\x9c'

# url=furl+one
# print(url)
# # url=url.encode("utf-8")
# # print(url)
# first=req.urlopen(url).read()
# fbea=bea(first,'html.parser')

# info=fbea.find_all(class_="api_txt_lines total_tit _cross_trigger")

# for a in info:
#      link = a.attrs['href']
#      text=a.text
#      print(text,link)
#      print()
# 해결해줘, 한글을 쳤을 때 .. 웹쪽에 한글 인코딩 방식이 다름.
# 그래서 맞춰줘야함.


# --------- 1-3
# from urllib.parse import quote_plus
# url="https://ko.wikisource.org/wiki/"
# url=url+quote_plus("저자")+":"
# typ=quote_plus(input())
# url=url+typ
# got=req.urlopen(url).read()
# soup=bea(got,'html.parser')
# k=soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li >ul")
# k_new=soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li >ul>li a")

# # find_all로 시도해보기.
# for i in k_new:
#      print(i.text,i.attrs['href'])# 시들의 공통점이 다 a가 있음. 따라서 위에 새로추가
#      print()
# # <a -> a는 태그, 뒤부터는 attributes

# for a in k_new:
#      print(a.attrs['title'], a.attrs['href'])
#      print()
     
#----------------
html="""
<ul id="bible">
  <li id="ge">Genesis</li>
  <li id="ex">Exodus</li>
  <li id="le">Leviticus</li>
  <li id="nu">Numbers</li>
  <li id="de">Deuteronomy</li>
</ul>
"""
hhtml="""
<html>
<body>
<div id="main-goods" role="page">
  <h1>과일과 야채</h1>
  <ul id="fr-list">
    <li class="red green" data-lo="ko">사과</li>
    <li class="purple" data-lo="us">포도</li>
    <li class="yellow" data-lo="us">레몬</li>
    <li class="yellow" data-lo="ko">오렌지</li>
  </ul>
  <ul id="ve-list">
    <li class="white green" data-lo="ko">무</li>
    <li class="red green" data-lo="us">파프리카</li>
    <li class="black" data-lo="ko">가지</li>
    <li class="black" data-lo="us">아보카도</li>
    <li class="white" data-lo="cn">연근</li>
  </ul>
</div>
</body>
</html>
"""
# k=req.urlopen(html).read()
# c=bea(hhtml,"html.parser")
# j=c.select("#ve-list>li.black")[1]

# print(j)
# #-----------------------------------

from bs4 import BeautifulSoup 
import re # 정규 표현식을 사용할 때 --- (※1)
html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")
# 정규 표현식으로 href에서 https인 것 추출하기 --- (※2)
li = soup.find_all(href=re.compile(r"^https://"))
print(li)
for e in li: 
     print(e.attrs['href'])
