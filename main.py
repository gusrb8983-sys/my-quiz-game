"""
나만의 퀴즈 게임 - 동물 편
main.py : 프로그램이 시작되는 파일
"""


class Quiz:
    """퀴즈 한 문제를 표현하는 설계도."""

    def __init__(self, question, choices, answer):
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


# ── 동물 퀴즈 5개를 Quiz 객체로 만들어서 리스트에 담아둔다 ──
DEFAULT_QUIZZES = [
    Quiz(
        question="세상에서 가장 큰 동물은?",
        choices=["아프리카코끼리", "대왕고래", "기린", "백상아리"],
        answer=2,
    ),
    Quiz(
        question="지상에서 가장 빠른 동물은?",
        choices=["치타", "사자", "말", "타조"],
        answer=1,
    ),
    Quiz(
        question="판다가 주로 먹는 음식은?",
        choices=["대나무", "물고기", "고기", "곤충"],
        answer=1,
    ),
    Quiz(
        question="다음 중 밤에 활동하는(야행성) 동물은?",
        choices=["부엉이", "닭", "비둘기", "참새"],
        answer=1,
    ),
    Quiz(
        question="다음 중 알을 낳는 포유류는?",
        choices=["오리너구리", "고양이", "코알라", "캥거루"],
        answer=1,
    ),
]


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

        if raw == "":
            print(f"⚠️ 아무것도 입력하지 않았습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        if not raw.isdigit():
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        number = int(raw)

        if number < min_value or number > max_value:
            print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        return number


def show_all_quizzes(quizzes):
    """저장된 퀴즈 전부를 화면에 뿌려본다."""
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    for index, q in enumerate(quizzes, start=1):
        q.show(index)
        print()


def play_quiz(quizzes):
    """퀴즈를 순서대로 출제하고, 정답 여부를 판정한 뒤 결과를 보여준다."""
    if not quizzes:
        print("😢 풀 수 있는 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
        return

    total = len(quizzes)
    print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")
    print("-" * 40)

    correct_count = 0

    for index, q in enumerate(quizzes, start=1):
        q.show(index)
        user_answer = ask_number("정답 입력: ", 1, 4)

        if q.is_correct(user_answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. 정답은 {q.answer}번입니다.")

        print("-" * 40)

    score = int(correct_count / total * 100)

    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)


def run():
    """메뉴를 반복해서 보여주고, 사용자의 선택을 처리한다."""
    while True:
        print_menu()
        choice = ask_number("선택: ", 1, 5)

        if choice == 1:
            play_quiz(DEFAULT_QUIZZES)
        elif choice == 2:
            print("👉 준비 중인 기능입니다. (퀴즈 추가)")
        elif choice == 3:
            show_all_quizzes(DEFAULT_QUIZZES)
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
    main()
