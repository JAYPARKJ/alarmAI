# 라이브러리 가져와 서비스 최적화 -> 필요한 클래스만 떼와서 수정 가능하다.

import random

ranint = random.randint(1, 10)
ranint2 = random.random()
# ranint2 덮어씌움 (마지막게 출력)
ranint3 = random.choice([ "사과", "바나나", "수박", "딸기"])

# 로또 1~46개 리스트 중 6개만 랜덤 세팅
rotto = random.sample(range(1, 46), 6)
 
print(ranint)
print(ranint2)
print(ranint3)
print(rotto)
# 컴퓨터는 랜덤이 없다 -> 왜? 기계가 랜덤을 어케? 씨드 
# 인공지능의 모든 값은 통계확률 



# 자바에서  크롤링 할 때 timesleep 쓴것 처럼 파이썬도 time을 쓴다
import time
print(time.time()) # 암호화된 현재 시간 
time.sleep(1) # 1초 쉬기 
print("시작")
time.sleep(5)

print("2")
time.sleep(2)
time.sleep(5)
print("종료")