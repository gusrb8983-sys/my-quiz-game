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

# 지금까지 기록된 최고 점수. 아직 한 번도 안 풀었으면 None 으로 둔다.
best_score = None


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


def ask_text(prompt):
    """빈 값이 아닌 글자를 입력할 때까지 계속 물어보고, 그 글자를 돌려준다."""
    while True:
        raw = input(prompt).strip()

        if raw == "":
            print("⚠️ 아무것도 입력하지 않았습니다. 다시 입력해주세요.")
            continue

        return raw


def list_quizzes(quizzes):
    """저장된 퀴즈 목록을 문제만 간단히 보여준다."""
    if not quizzes:
        print("📋 등록된 퀴즈가 없습니다.")
        return

    print(f"📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("-" * 40)

    for index, q in enumerate(quizzes, start=1):
        print(f"[{index}] {q.question}")

    print("-" * 40)


def play_quiz(quizzes):
    """퀴즈를 순서대로 출제하고, 정답 여부를 판정한 뒤 결과를 보여준다."""
    global best_score  # 이 함수 안에서 바깥의 best_score를 직접 바꾸겠다는 선언

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

    if best_score is None or score > best_score:
        best_score = score
        print("🎉 새로운 최고 점수입니다!")

    print("=" * 40)


def add_quiz(quizzes):
    """새 퀴즈를 입력받아 quizzes 리스트에 추가한다."""
    print("📌 새로운 퀴즈를 추가합니다.")

    question = ask_text("문제를 입력하세요: ")

    choices = []
    for i in range(1, 5):
        choice = ask_text(f"선택지 {i}: ")
        choices.append(choice)

    answer = ask_number("정답 번호 (1-4): ", 1, 4)

    new_quiz = Quiz(question=question, choices=choices, answer=answer)
    quizzes.append(new_quiz)

    print("✅ 퀴즈가 추가되었습니다!")


def show_score():
    """지금까지의 최고 점수를 보여준다."""
    if best_score is None:
        print("😅 아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어보세요!")
        return

    print(f"🏆 최고 점수: {best_score}점")


def run():
    """메뉴를 반복해서 보여주고, 사용자의 선택을 처리한다."""
    while True:
        print_menu()
        choice = ask_number("선택: ", 1, 5)

        if choice == 1:
            play_quiz(DEFAULT_QUIZZES)
        elif choice == 2:
            add_quiz(DEFAULT_QUIZZES)
        elif choice == 3:
            list_quizzes(DEFAULT_QUIZZES)
        elif choice == 4:
            show_score()
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
