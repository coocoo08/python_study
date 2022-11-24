'''
    1. 상속 : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용.

                            몬스터

                땅몬스터    물몬스터    공중몬스터

    2. 부모 클래스 정의
        - 속성
            - 이름, 체력, 공격력
        - 함수
            - 이동하기 (move)
'''

# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"[{self.name}] 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):       # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날기")

wolf = Wolf("울프", 1500, 200)
wolf.move()

shark = Shark("샤크", 3000, 400)
shark.move()

dragon = Dragon("드래곤", 8000, 800)
dragon.move()