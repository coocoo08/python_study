'''
    for 변수 in 시퀀스 자료 :
        명령문

    예) for a in [1, 2, 3, 4]
        print(a)

    * 순서가 있는 자료형
     - 리스트, 문자열, range객체, 튜플, 딕셔너리
'''

# 리스트 사용
champions = ['티모','이즈리얼', '나미']

for champion in champions:
    print("선택한 챔피언은", champions, "입니다")

# 문자열 사용
message = "나는 할 수 있어! 다 할 수 있어!"
for word in message:
    print(word)

# range 객체 사용
x = range(10)
for i in x:
    print(i)

print()
# range(시작, 끝 + 1, 단계)
for i in range(1, 10, 2):
    print(i)













