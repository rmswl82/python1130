#try1.py

#함수를 정의
def divide(a,b):
    return a/b

#에러 처리
try:
    #함수를 호출
    result = devide(5,2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다")
except:
    print("다른 에러

#함수를 호출
result = devide(5,0)
print("결과:{0}".format(result))

print("전체 코드 실행 종료")
