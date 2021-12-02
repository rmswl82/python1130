#DemoStr.py

names = ["전우치", "홍길동", "이순신"]
for name in names:
    print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
    print("="*40)

strA= "python is very powerful"
print(len(strA))
#첫글자를 대문자로
print(strA.capitalize())
print(strA.count("p"))
#구간을 슬라이싱해 7번째부터 p가 몇개인지
print(strA.count("p", 7))

print("demo.ppt".endswith("ppt"))
print("mbc2580".isalnum())
print("mbc:2580".isalnum())
print( "2580".isdecimal())

strB = " spam and ham "
print(strB)
#결과값을 반드시 받아서 처리, 위 아래 결과 비교
#특정문자열 삭제
result = strB.strip()
print(result)

strC = "<<< spam and ham >>>"
print(strC)
result = strC.strip("<> ,")
print(result)

result = result.replace("spam", "spam and egg")
print(result)
#분리
lst = result.split()
print(lst)
print("___다시 하나로___")
print(" ".join(lst))

#정규 표현식
import re

string = "<<< data << data"
result = re.sub("<<<", "<<", string)
print(result)

#특정 문자열 패턴: 숫자가 0~n번 th
result = re.match("[0-9]*th", "35th")
result2 = re.search("[0-9]*th", "35th")
#매칭 오브젝트
print(result)
print(result2)

#연도를 검색
result = re.match("\d{4}", "올해는 2021년입니다")
print(result)
result = re.search("\d{4}", "올해는 2021년 입니다")
print(result)
#찾은 값을 보여줘
print( result.group() )


#우편번호를 검색
result = re.search("\d{5}", "우리 동네는 52300입니다")
print( result.group())
