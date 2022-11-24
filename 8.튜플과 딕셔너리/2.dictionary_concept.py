'''
    1. 딕셔너리
        - 시퀀스 자료형
        - 키와 데이터를 가지고 있는 사전형 자료형
        - 사전형태의 자료를 만들 때 편리
        - 사전형태의 자료형

        딕셔너리 = {키1 : 데이터1, 키2 : 데이터2}

    2. 딕셔너리 접근하기
        딕셔너리["키"]

        딕셔너리 할당하기
         딕셔너리["키"] = 데이터

        딕셔너리 삭제하기
         del 딕셔너리["키"]
'''

#딕셔너리 만들기
stock_a = {"삼성전자" : 61000, "LG전자" : 90400}

stock_b = {
    "삼성전자" : [61000, 61500, 62000, 62500, 62000],
    "LG전자" : (90400, 90900, 90300, 90420, 90401)
}

stock_c = {
    '삼성전자' : {
        "현재가" : 61000,
        "보유수량" : 5,
        "매수단가" : 60000
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

#딕셔너리 할당하기
stock_a["삼성전자"] = 65000
print(stock_a)

#딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 61000,
    "SK하이닉스" : 86100,
    "NAVER" : 186000,
    "카카오" : 57100
}

# items() : 키와 데이터 쌍
for item in stock_d.items():
    print(item)

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)














