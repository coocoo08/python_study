# 함수의 입력 parameter의 개수를 모를 때
# *(aserisk)를 앞에 붙이는 것으로 여러개의 parameter를 받아서 tuple로 변환해줌

def add_many(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4, 5))
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
