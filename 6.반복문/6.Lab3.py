'''
    순신은 lily라는 이름의 교환학생과 친해지게 되었습니다.
    영어를 잘하지 못하는 순신은 lily에게 한국어를 가르쳐 주기 위해
    한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다
        - 리스트에서 순서대로 단어를 가져와 화면에 출력한다
        - 프로그램 사용자는 단어를 그대로 입력하고
        - 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료.

        Let's Learning Korean
        사랑해
        사랑해
        귀엽다
        귀엽다
        고마워
        고마워
        행복해
        햄복해
'''

world_list = ["사랑해", "귀엽다", "고마워", "징글징글해", "배고파", "어깨아파", "언제끝나", "안끝나"]
print("Let's Learning Korean")
for word in world_list:
    print(word)
    write = input()
    if word != write:
        break

