'''
    * 리스트 자료형
        - 리스트명 = [데이터, 데이터, 데이터, ....]
'''

# 데이터가 없는 리스트
empty = []

# 데이터가 있는 리스트
earPods = ["액티브 노이즈 캔슬링", "적용형 주변음 허용 모드", "터치 제어", "개인 맞춤형 공간 음향"]

# 데이터 접근하기
# 인덱스는 0부터 시작함
print(earPods[2])
print(earPods[-1])

# 데이터 추가하기
earPods.append("강한 생활 방수 디자인")
print(earPods)

# 데이터 할당하기
earPods[1] = '기기 간 자동 전환'
print(earPods)

# 데이터 삭제하기
del earPods[0]
print(earPods)

# 리스트 슬라이싱
print(earPods[1:3])
print(earPods[:])
print(earPods[:3])
print(earPods[1:])

# 리스트 길이
print(len(earPods))

# 리스트 정렬
earPods.sort()
print(earPods)















