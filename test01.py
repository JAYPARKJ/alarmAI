# 문장 거꾸로 출력해보기
text = input("문장을 입력하세요:")
# 문자열 -> 배열을 거꾸로~ 
print(text[::-1])

# 이메일에서 아디만 출력해보기 
email = input("이메일을 입력하세요:")
# abcd0000@gmail.com
# '@' 기준으로 앞에만 출력한다.
id = email.split("@")[0]
print("당신의 아이디는:", id)
