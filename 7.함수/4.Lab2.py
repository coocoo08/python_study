'''
    로또 예상번호 추출 프로그램을 구현하려고 합니다.
    다음 조건에 따라 프로그램을 완성해 보시오.
        1) 로또 번호를 6개를 생성한다
        2) 로또 번호는 1~45까지의 랜덤한 번호다
        3) 6개의 숫자 모두 달라야 한다
        4) get_random_number() 함수를 사용해서 구현한다.

        출력 예) 1 8 11 13 26 42

        - 리스트, 반복문, 조건문
'''
import random
def get_random_number():
# 로또 번호를 저장할 리스트
    list =[]
# 현재 뽑은 숫자 개수
    count = 0
    for lotto in range(1, 7, 1):
        number = random.randint(1, 45)
        if number not in list:
            list.append(number)
        elif number in list:
            number = random.randint(1, 45)
            list.append(number)
    list.sort()
    print(list)
    return number

get_random_number()

def get_random_number2():
#로또 번호를 저장할 리스트
    lotto_num =[]
# 현재 뽑은 숫자 개수
    count2 = 0
    while True:
        if count2 > 5:
            break
        random_number = get_random_number2()
        if random_number not in lotto_num:
            lotto_num.append(random_number)
            count2 += 1

    lotto_num.sort()
    for num in lotto_num:
        print(num, end=' ')