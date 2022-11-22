'''
    사용자로부터 국어, 수학, 영어 성적이 입력됩니다.
    세 과목의 평균점수가 80점 이상이면 합격입니다.
    그런데 프로그램의 오류가 발생했습니다.
    80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해 보시오.
    (단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력했습니다"를 출력하시오)

    예시)
        국어 >>>
        수학 >>>
        영어 >>>

        불합격       합격      잘못 입력했습니다
'''

# 방법1
kor = float(input("국어 >>> "))
math = float(input("수학 >>> "))
eng = float(input("영어 >>> "))
avg = (kor + math + eng) / 3
if 0 <= kor <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
    if avg >= 80:
        print("불합격")
    elif avg >= 0:
        print("합격")
else:
    print("잘못 입력했습니다.")

# 방법2
if kor < 0 or kor > 100 or math < 0 or math > 100 or eng < 0 or eng > 100:
    print("잘못 입력했습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")