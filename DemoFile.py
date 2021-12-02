# DemoFile.py
import sys
#구분자 sep 끝문자 end
print("hello", "python", sep="~", end="!", file = sys.stderr)

#파일을 다루는 객체를 생성
f = open("c:\\work\\domo.txt", "wt")
print("파일에 쓰는 작업", file = f)
f.close()

#문자열을 결합하는 경우
url = "http://www.naver.com/?page="+str(1)
print(url)

#문자열 정렬
for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("___오른쪽 정렬___")
for x in range(1,6):
    #문자로 바꾸고 rjust 오른쪽으로 붙여 정렬, 자릿수는 3자리
    print(x, "*", x, "=", str(x*x).rjust(3))

print("___0으로 채우기___")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(3))