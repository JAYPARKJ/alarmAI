# a = 0
# for i in range(5):
#     i+a 

# print(a)

# a = 0
# for i in range(5):
#     ａ＝ i+a 
#     print(a)    


a = 0
for i in range(5):
    a = i + a
    print(a)


'''
for i in [0,1,2,3,4]:
    print(i)

for i in range(5):
    print(i)

for i in range(0,5):
    print(i)

for i in range(0,5,1):
    print(i)

for i in [0,1,2,3,4]:
    print(i)
    print("------------")

for i in [0,1,2,3,4]:
    print(i)
    print("------------) for문 영역
    ** tab 들여쓰기가 중요하다.**
print("--------") for문이 아님 
'''

a=0
for i in range(5):
    i+a
print(a) # 0

a=0
for i in range(5):
    a = i+a
print(a) # 10


# 이중 for문 
'''
vision = ['happy', 'smart', 'enjoy']
city = ['seoul', 'busan', 'ulsan']

for x in vision:
  for y in city:
    print(x, y)
'''
# quiz 이중 for : 성이 "김", "이", "박"과 이름이 "재욱","지수","제니"로 만들수 있는 
# 이름을 이중 for문을 활용하여 출력하세요
# 문자열은 그 자체로 반복 가능한(iterable) 자료형이라서 for 문에 바로 쓸 수 있어!
성  = {"김", "이", "박"}
이름 = {"재욱", "지수", "제니"}

# 이중 for문
for i in 성:
   for j in 이름:
       print(성, 이름)

for i in 성:
    for j in 이름:
        print(i+j)


# end-1
for i in range(1, 10):
   for j in range(1,10):
        #print(f"{{i} x {j} = {i * j} 
        print(f"{i} x {j} = {i*j}")


surname = ["김", "이", "박"]
name = ["재욱", "지수", "제니"]

for s in surname:
    for n in name:
        print(s+n)
        

# 돈
money = True

# 돈이 있따면?
if money : 
    print('택시 타고가기')
else : 
    print('걸어간다')

'''
들여쓰기 중요
if 조건문 : 
    수행_문장1
    수행_문장2
else :
    수행_문장1
    수행_문장2
else는 필수가 아니다
'''


'''
and
or
not
'''

'''
in 
not in
'''
money = 3000
pocket = ['paper', ' cellphone', 'money']
if money in pocket:
    print('xortlxkfk')

# if와 elif 차이 없다. 메모리 적으로 조금 좋다 

# while 
i = 0
while i < 101:
    i+=1
    if i % 11 == 0:
        print("11의배수",i)
    elif i % 3 == 0:
        print("11의배수",i)
    elif i % 5 == 0:
        print("5의배수",i)
    else:
        continue

# Continue 다음 for로 돌아갈 때 
# pass 다음줄로 내려갈 때 
i = 0
while i < 101:
    i+=1
    if i % 11 == 0:
        print("11의배수",i)
        pass
    elif i % 3 == 0:
        print("11의배수",i)
        pass # continue 일 경우 for문으로 올라가 i를 바꿔준다 
        
    elif i % 5 == 0:
        print("5의배수",i)
        pass 
    else:
        continue

# break는 멈춤i = 0
while i < 101:
    i+=1
    if i % 11 == 0:
        print("11의배수",i)
        break
    elif i % 3 == 0:
        print("11의배수",i)
    elif i % 5 == 0:
        print("5의배수",i)
    else:
        continue

# 무한루프 계속 참일 때 돌아감
while True:
    num = int(input("1번:이름 2번:주소 3번:나가기"))
    if num ==1:
        print("김재욱",i)
    elif num ==2:
        print("서울시")
    elif  num ==3:
        print("3번 종료")
        break
    else:
        print("다음 버튼을 눌러주세요")

# quiz : 나무 10개를 하나씩 때려서 트리를 만들라?
tree = 10
while (tree > 0):
    (input("나무를 때린다 "))
    #tree =  tree - 1
    tree -=1
    print(f"남은 나무 : {tree}")
print("나무가 없어요")


tree = 10
while (tree > 0):
    num = int(input("숫자 입력:"))
    #tree =  tree - 1
    tree -= num
    print(f"남은 나무 : {tree}")
print("나무가 없어요")

# quiz 입력값을 받아 짝수인지 홀수인지 판별해라
# boolean이 0과 1이니 
while True:
    num = int(input("숫자를 입력하세요"))
    if num % 2 == 0: 
        print(f"{num}는 짝수입니다")
    else : print(f"{num}는 홀수입니다")
    continue


# 만약 100이 될 때 종료
i = 0
while i < 100:
    num = int(input("숫자 입력:"))
    if num % 2:
        print(f"{num}는 짝수입니다")
    else: print(f"{num}는 홀수입니다")

 