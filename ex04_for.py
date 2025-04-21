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

 
 