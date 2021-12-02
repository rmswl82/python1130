# web1.py

#웹 페이지 크롤링(수집)

from bs4 import BeautifulSoup
#페이지 로딩
#메서드 체인: 연속으로 호출하기 가능 open과 read 함수 모두 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
#웹에 있는 데이터 가져올때 상수처럼 html.parser을 씀
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
#첫번째 p 태그만 가져와
print(soup.find("p"))

print("*"*40)

#조건이 있는 경우(필터링)
#<p class="outer-text">컨텐츠</p>
#파이썬의 키워드로 class가 제공
print( soup.find_all("p", class_="outer-text") )

print("*"*40)

#태그 안쪽의 문자열 가져오기
for item in soup.find_all("p"):
#앞위에 태그를 버리고 컨텐츠만 가져오기(.text 속성)
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)



