# 변수
# 변수이름 = 데이터
# 변수 이름 짓는 규칙 - 문자부터 시작해야 함.
#                  - 대소문자는 구분함.
#                  - _로 시작할 수 있음.
name = "마스터 이"
level = 5
health = 800
attack = 90
print(name, level, health, attack, sep=", ")

# 변수에 저장된 데이터 변경하기
level = level + 1       # 5 + 1
health = health + 50    # 800 + 50
attack = attack + 10    # 90 + 10
print(name, level, health, attack, sep=", ")