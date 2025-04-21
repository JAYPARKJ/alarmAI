'''
함수 def를 쓴다.
def 함수이름(매개변수):
    실행 코드
    return 결과

'''

def add(a, b):
    num = a + b
    return num

print(add(3,6))

# 이름과 나이를 입력하면 나는 {name} 이고 {age}살 입니다
name = "jay"
age = 31
def mine(name, age):
    me = f"{name}이고 {age}살"
    return me
   # print(f"{name}이고 {age}")
print(mine("jay", 31))

def me(name, age):
    me = f"{name}이고 {age}살"
   # print(f"{name}이고 {age}")
me("jay", 31)

# self의 주소가 나온다 (객체 자체가 나옴)
# print(self) 

# def me(name, age):
#     me = f"{name}이고 {age}살"
   # print(f"{name}이고 {age}")

 

# print는 찍어내기, return 밖으로 

def sum(a,b):
    num = a + b
    return num 
sum(3,6)

def mul(a,b):
    num = a * b
    return num
mul(3,6)
def div(a,b):
    num = a / b
    return num
div(3,6)
def mod(a,b):
    num = a % b
    return num
mod(3,6)

## 주요함수 ## enumerate : 인덱스와 값 함께
 
# 인덱스를 알고 싶다
ex_list = ["김밥", "치킨", "우동", "라면"]
for idx in enumerate(ex_list):
    print("인덱스 : ", idx, "음식:", li)

# zip : 리스트 묶어서 반복한다.

# 라이브러리 - conda, 표준 : 이미 있는것 pip
# 설치는 pandsa == 두개 
