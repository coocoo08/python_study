'''
    1. while 사용법
    초기식
    while 조건식 :
        반복할 명령
        증감식

    2. 무한루프와 break
    while True :
        반복할 명령
        if 조건식 :
            break
'''

i = 0       #초기식
while i < 10:   #조건식
    print(i, "번째 다짐. 나는 할 수 있쪄!")
    i += 2      #증감식
print()
#무한루프 : 조건식에 True를 넣어서 항상 반복되게 만든 것
while True:
    x = input("종료하려면 exit를 입력하세요>>> ")
    if x == "exit":
        break