'''
    1. 클래스
        - 속성
            - 체력
            - 공격력
            - 방어력
            - 이동속도
        -메서드
            - 위치로 이동하기
            - 공격하기
            - 아이쳄 사용하기
            - 귀환하기
    2. 클래스 만들기
        class 클래스이름 :
            def 메서드이름(self) :
                명령블록

    3. 클래스 사용하기
        인스턴스 = 클래스이름()
        인스턴스.함수()
'''
class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신 것을 환영합니다.")

    def basic_attack(self):
        print(f"{self.name} 기본 공격 {self.attack}")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 750, 92)

ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()








