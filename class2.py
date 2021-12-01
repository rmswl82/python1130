# class2.py
#1) 클래스 형식을 정의

class Person:
    #클래스에 소속된 데이터 공유하는 멤버 변수
    num_person = 0

    #생성자(초기화)메소드
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
        #클래스 자체에 소속된 의미
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
print("인스턴트 갯수:{0}".format(Person.num_person))

#특정 인스턴스에 변수를 추가
p1.age = 30
print(p1.age)
# #p2 멤버변수가 없으므로 attributeerror 에러 메시지
# print(p2.age)




