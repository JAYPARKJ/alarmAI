a = [1,2,3,4,5,6]
print(len(a))

# del : 인덱스 삭제
del a[1]
print(a)

# ★추가하기★
b = [1,2,3]
b.append(4)
print(b)

# 정렬하기
c = [4,3,2,1]
c.sort()
print(c)

# 반대 reverse
c = [3,2,4,1]
c.reverse()
print(c)

a = [3,2,4,1]
# 헷갈 ㄴㄴ, 3을 찾는거, 0나옴
print(a.index(3))

# 삽입하기 
a = [1,2,3]
a.insert(0, 4)
print(a)

# 삭제 
a = [1,2,3,3]
a.remove(3)
print(a)

# ★ pop ★
a = [1,2,3,3]
b = a.pop(3)
print(a) # [1,2,3] 3을 꺼냄
print(b) # 3 꺼낸것을 프린트 

# 개수 세기 
a = [1,2,3,3]
print(a.count(3))

# 튜플 - 수정이나 삭제 X
# 딕셔너리 - 키를 기준으로 찾는 자료형 
 




