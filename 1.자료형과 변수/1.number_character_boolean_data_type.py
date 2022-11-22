# 주석(comments)
# 숫자형 - 숫자 데이터, 정수형, 실수형
# 문자열 - 문자를 나열한 것
#       - "(큰따음표) 또는 '(작은따음표)로 문자열의 시작과 끝을 나타냄
#       - ' "" '
#       - " '' "
#        """
#           여러줄에 걸쳐 문자열 표현 가능
#        """
#       - indexing & slicing string
#           - 문자열의 각 문자는 순서가 있음
#           - 이때 각 문자열의 순서를 인덱스라고 함
#           - 첫번째 시작문자의 순서는 0으로 시작 (1이 아님)
#           - -1 인덱스 : 가장 마지막 인덱스, -2 : 마지막에서 두번째 인덱스를 의미...
#           - 문자열 slicing
#               - 인덱스가 하나의 문자만을 추출함
#               - slicing은 부분 문자열을 추출함
#               - [시작:끝]에 해당하는 부분 문자열을 추출함
#       - 문자열 함수
#           - format()
#               - 문자열내의 특정함 값을 변수로부터 초기화하여 동적으로 문자열을 생성

# 불린형 - 참 또는 거짓 (True or False)
# None - 아무런 값을 갖지 않을 때 사용
#        해당 변수가 초기값을 갖지 않게 하여 생성할 때 사용

'''
 print()
    - ,(콤마)로 여러 변수를 나열하면 한줄로 출력
    - 기본적으로는 한칸 띄어쓰기 후 출력
'''

print(1, 3, 0, -1, sep=', ')
print(1.1, 3.1, 0, -1.4, sep=', ')
print("침묵은 과학입니다.")
print('현대 침묵의 경이로움')
print('"노이즈 캔슬링"')
print(True)

a = 10
b = 11.4
print(a, b, 10, 100, sep='*', end='||')
print(a, b)

print(type(a))
print(type(b))

c = None
print(c)

d = ''' Hello
        Ezen!
    '''
e = """
        Hello
    world!
    """
print(d)
print(e)

f = 'Hello World'
print(f[10])
print(f[0])
print(f[-1])
print(f[-11])
#print(f[11])       # 범위를 넘어갈 경우 에러 발생
print(f[0:11])
print(f[0:1])
print(f[:5])
print(f[3:])
print(f[:])

print(f.upper())
print(f.replace('H', 'j'))

temperature = 15.5
prob = 50.0

g = '오늘 기온{}도 이고, 비 올 확률은 {}% 입니다.'.format(temperature, prob)
print(g)









