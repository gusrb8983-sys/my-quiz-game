"""
나만의 퀴즈 게임 - 동물 편
main.py : 프로그램이 시작되는 파일
"""


class Quiz:
    """퀴즈 한 문제를 표현하는 설계도."""

    def __init__(self, question, choices, answer):
        # 이 퀴즈가 가지고 있는 정보(속성)를 자기 몸에 새겨 넣는다
        self.question = question   # 문제 (글자)
        self.choices = choices     # 선택지 4개 (목록)
        self.answer = answer       # 정답 번호 (1~4 중 하나)

    def show(self, number):
        """문제와 선택지를 화면에 출력한다."""
        print(f"[문제 {number}] {self.question}")
        for index, choice in enumerate(self.choices, start=1):
            print(f"  {index}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 낸 답이 정답인지 True / False 로 알려준다."""
        return user_answer == self.answer


def print_menu():
    """메뉴 화면을 출력한다."""
    print()
    print("=" * 40)
    print("🐾 나만의 동물 퀴즈 게임 🐾")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def ask_number(prompt, min_value, max_value):
    """올바른 숫자를 입력할 때까지 계속 물어보고, 그 숫자를 돌려준다."""
    while True:
        raw = input(prompt).strip()

        # 1) 그냥 Enter만 누른 경우
        if raw == "":
            print(f"⚠️ 아무것도 입력하지 않았습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        # 2) 숫자가 아닌 글자를 입력한 경우 (예: abc)
        if not raw.isdigit():
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        number = int(raw)

        # 3) 숫자지만 범위를 벗어난 경우 (예: 9)
        if number < min_value or number > max_value:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        # 여기까지 왔다면 올바른 입력이다
        return number


def demo_quiz():
    """3단계 확인용 임시 함수 (다음 단계에서 삭제합니다)."""
    q = Quiz(
        question="세상에서 가장 큰 동물은?",
        choices=["아프리카코끼리", "대왕고래", "기린", "백상아리"],
        answer=2,
    )

    q.show(1)
    print("정답은 2번:", q.is_correct(2))   # True 가 나와야 정상
    print("정답은 3번:", q.is_correct(3))   # False 가 나와야 정상


def run():
    """메뉴를 반복해서 보여주고, 사용자의 선택을 처리한다."""
    while True:
        print_menu()
        choice = ask_number("선택: ", 1, 5)

        if choice == 1:
            print("👉 준비 중인 기능입니다. (퀴즈 풀기)")
        elif choice == 2:
            print("👉 준비 중인 기능입니다. (퀴즈 추가)")
        elif choice == 3:
            print("👉 준비 중인 기능입니다. (퀴즈 목록)")
        elif choice == 4:
            print("👉 준비 중인 기능입니다. (점수 확인)")
        elif choice == 5:
            print("👋 게임을 종료합니다. 안녕히 가세요!")
            break


def main():
    """프로그램 시작점. 강제 종료 상황에서도 안전하게 끝내도록 감싼다."""
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        print()
        print("👋 프로그램을 안전하게 종료합니다.")


if __name__ == "__main__":
    # demo_quiz()
    main()