#   비만도 계산기를 만들어 보시오.
#   예시)
'''
예시)
        BMI 계산기 입니다.
        신장 : (입력)
        몸무게 : (입력)
        BMI :

'''
print("BMI 계산기 입니다.")
tall = float(input("신장 : "))
weigh = float(input("몸무게 : "))
print("BMI : ", round(weigh / (tall * tall) * 10000, 2))