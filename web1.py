# web1.py

#웹 페이지 크롤링(수집)

from bs4 import BeautifulStoneSoup
#페이지 로딩
#메서드 체인: 연속으로 호출하기 가능 open과 read 함수 모두 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

