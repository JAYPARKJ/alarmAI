a = "20250421Sunny"
# 슬라이싱 방법으로 해보기 
year = a[0:4] 
# 정답 year = a[:4]
month = a[4:6]
day = a[6:8]

# weather = a[8:13]
 # a[8:]
# print(year, month, day, weather)
# 문자열은 immutable = 원본 못 바꿈

# replace()는 새로운 문자열을 반환
# 원래 변수에 재할당해야 반영됨

a ="pithon"
a= a.replace("i", "y")
print(a)

# 오답
a = "pithon"
a.replace(a[-4], 'y')
# a.replace(a[-4], 'y') -> tuple이 아니라서 오답
# 슬라이싱 후 얘 하나만 바꾸기 
# replace -> i : y

#정답
# b = a[:1] + 'y' + a[2:]
# print(b)

a = "condinf"
b = a[:-1] + 'g'
print(b)

# 다양한 포맷팅
print("나는 %d번 버스를 탄다" % 100)
print("나는{0}번 버스를 탄다".format(100))

# print(f"나는 {100}번 버스를 탄다  ")
# .format 함수를 f-string
a = "나는{0}번 버스를 탄다".format(100, 23)
print(a)

a = "나는{0}번 버스를 타고 {address}번지로 간다.".format(100, addrees=23)
print(a) 

# bus = 100
# address = 23
# a = f"나는 {bus}번 버스를 타고 {address}번지로 간다"
# print(a)

# bus = 100
# address = 23
# a = f"나는 {bus+1}번 버스를 타고 {address}번지로 간다"
# print(a)


# name = "철수"
# age = 25
# a = f"{name}는 {age}살입니다."
# print(a)

