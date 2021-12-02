# web2.py

#웹 서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

# <td class="title">
# 		<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>


data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
soup = BeautifulSoup(data, "html.parser")

#검색이 용이한 객체 soup
#find_all은 리스트로 결과를 담아줌
cartoons = soup.find_all("td", class_="title")
print("갯수{0}".format( len(cartoons) ))
#첫번째 방에 있는 것을 슬라이싱
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text.strip()
    print(title)
    