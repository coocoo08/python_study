# lambda 함수
'''
    - 굉장히 간단한 함수가 있는 경우, 한 줄짜리 함수로 간편하게 사용 가능
'''

def add(a, b):
    return a + b

f = lambda a, b: a + b
print(f(3, 5))
print(add(3, 5))

def get_length(s):
    return len(s)

#글자 길이에 따른 정렬
strings = ['Meet', 'the most', 'rugged', 'and']
strings.sort(key=lambda s:len(s))
print(strings)

# 수학 계산
import math
number = 3.14

# 절대값, 올림, 내림
print(abs(number))
print(math.ceil(number))
print(math.floor(number))

# sin, cos
print(math.sin(number))
print(math.cos(number))







