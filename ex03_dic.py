# dic = {"name":"jiwon", "age":"10", "birth":"0503"}
# print(dic)

# 나이 추가 
# dic = {"name:", "박지원"}
# dic["나이"] = "10"
# print(dic)

# 값 삭제
# dic = {"name:": "박지원","나이":"10"}
# del dic["나이"]  
# print(dic)

# dic = {"name":"jiwon", "age":"10", "birth":"0503"}
# a = dic.keys
# print(a)

# dic = {"name":"jiwon", "age":"10", "birth":"0503"}
# a = dic.values
# print(a)

# dic = {"name":"jiwon", "age":"10", "birth":"0503"}
# a = dic.items()
# print(a)

# 학생 나이 모으기
# age = [21,23,10,26,30]
# name = ["김재욱", "제니", "애순", "진", "카리나"]
# dic 만들 때 키와밸류

# 집합
# 중복 허용 하지 않는다, 순서가 없다
# ex_set = set('hello')
# print(ex_set)

'''
교집합
합집합
차집합

'''

'''
boolean : True, False
값이 있으면 True
"" : False

'''

'''
변수와 상수
변수 : 파이썬에서 데이터저장하고 추후에 사용할 수 있게 해주는 메모리 공간 
상수 : 대문자
'''

# quiz
a = "hello"
print(a[4]+a[3]+a[2]+a[1]+a[0])
print("".join(reversed(a)))

print(a[::-1])

# join, reverse
print(",".join("abcd"))
print("".join(a.reverse()))

# quiz 2
my_list = []
my_list.append('김밥')
my_list.append('라면')
my_list.append('치킨')

# 방법2 
my_list.append(["김밥", "라면", "치킨"])
# 이중 리스트로 나옴 -> for문 

print(my_list) # 변수[키-값]
# quiz 3
hobbies = {"Jaeuk": "soccer", "Jane":"reading", "Mike":"gaming"}
#hobbies["soccer"] = "drawing"
hobbies["Jaeuk"] = "drawing"

# 왜 변수 안넣었지
hobbies["sarah"]="music"
del hobbies["Jane"]

# append 넣으려면 초기화
hobbies["sarah"] = []
hobbies["sarah"].append("music")
#hobbies["sarah"] = "music"
#hobbies["sarah"].append("music")
print(hobbies)
 