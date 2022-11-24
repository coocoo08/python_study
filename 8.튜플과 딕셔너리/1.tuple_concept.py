'''
    1. 튜플(Tuple)
        1) 시퀀스 자료형
        2) 수정, 추가, 삭제가 불가능한 리스트
        3) 읽기만 가능하기 때문에 데이터 손실 염려가 없음
        4) 메모리 사용이 효율적임

    2. 튜플 만들기
        튜플 = (데이터, 데이터, 데이터)
        튜플 = 데이터, 데이터, 데이터

        a = (3, 4, 5)
        a = "이젠IT아카데미", 3, True

        a = (30,)
        a = 30,

    3. 튜플을 리스트로 만들기

    4. 패킹과 언패킹
        - 패킹 : 여러개의 데이터를 하나의 변수에 할당하는 것
        - 언패킹 : 컬렉션의 각 데이터를 각각의 변수에 할당하는 것

        numbers = 3, 4, 5    numbers = [3, 4, 5]      # 패킹
        a, b, c = numbers    a, b, c = numbers        # 언패킹

    5. 튜플 함수
'''

# 튜플 : 읽기 전용 리스트
a = (3, 4, 5)
b = 3, 4, 5

print(type(a))
print(type(b))

c = (3,)
d = 3,

print(type(c))
print(type(d))

e = tuple([3, 4, 5])
print(type(e))
f = list(e)
print(type(f))
g = list(range(10))
print(type(g))
h = tuple(g)
print(type(h))

i = 3, 4, 5
j = list(i)
print(type(j))

# 튜플 관련 함수
x = 5, 6, 7, 8
print(max(x))
print(min(x))
print(sum(x))
print(x.count(6))       #특정값의 개수
print(x.index(7))       #특정값의 인덱스 구하기



