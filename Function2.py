# Function2.py

#함수 정의
def change(x):
    x[0] = "H"
    
#함수를 호출
wordlist = ["j", "a", "m"]
#pass by reference

change(wordlist)
print("함수 호출 후:", wordlist)

#지역변수와 전역변수(이름 호출)

x=1
def func(a):
    return x+a
#호출
print(func(1))

def func2(a):
    x=2
    return x+a

#호출
print(func2(1))
