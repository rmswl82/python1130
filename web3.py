#web3.py
#크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
soup = BeautifulSoup(data, "html.parser")
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#페이지 1번에서 5번
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

# ctrl + / 
# <td class="title">
# 		<a href="/webtoon/detail">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format( len(cartoons) ))
#첫번째 방에 있는 것을 슬라이싱 
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text.strip()
    print(title)
f.close()
print("웹 크롤링 종료~~")
