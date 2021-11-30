# Function3.py

# 함수의 기본값이 있는 경우
def times(a=10, b = 20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))


# 키워드, 인자
def userURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출

print(userURI("credu.com", "80"))
print(userURI(port = "8080", server = "credu.com"))

#가변인자는 입력되는 인자의 갯수가 가변적인 경우
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))




