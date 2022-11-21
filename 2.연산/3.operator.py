# 대입연산, 산술연산, 비교연산, 논리연산

x = 5
y = 2

# 산술연산
#   - 연산자                       설명
#   -  //                          몫
#   -  **                         제곱
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱

# 문자열 연산
tag1 = "#노이즈 캔슬링 마이크"
tag2 = "#후면 통풍구"
tag3 = "#외부 소리 감지"

tag = tag1 + tag2 + tag3
print(tag)

massage = "우린 모두 파이썬을 사랑합니다. \n" * 5
print(massage)

#복합대입연산자
level = 10
level += 1 #level + 1 # 레벨 1 증가

health = 2000
health -= 300#health = health - 3000 # cpfur 300 갑소

attack = 300
attack *= 1.5 #공격력 1.5배 증가

speed = 420
speed /= 2 #이동속도 50% 감소

print(level, health, attack, speed)