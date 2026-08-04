"""
나만의 퀴즈 게임 - 동물 편
main.py : 프로그램이 시작되는 파일
"""

import json
import os

STATE_FILE = "state.json"   # 퀴즈와 최고 점수를 저장할 파일 (프로젝트 루트)


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


# ── 동물 퀴즈 5개. state.json이 없거나 손상됐을 때 쓸 기본 데이터 ──
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


class QuizGame:
    """게임 전체를 관리하는 설계도.
    퀴즈 목록과 최고 점수를 속성으로 가지고,
    메뉴 표시/퀴즈 풀기/추가/목록/점수 확인/저장·불러오기를 메서드로 제공한다."""

    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.load()   # 프로그램이 시작될 때 저장된 데이터가 있으면 불러온다

    # ── 파일 저장 / 불러오기 ──────────────────────────────

    def load(self):
        """state.json에서 데이터를 불러온다.
        파일이 없거나 손상되었으면 기본 퀴즈 데이터로 시작한다."""

        if not os.path.exists(STATE_FILE):
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = None
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in data["quizzes"]
            ]
            self.best_score = data.get("best_score")

            score_text = self.best_score if self.best_score is not None else "없음"
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {score_text})")

        except (json.JSONDecodeError, KeyError, TypeError):
            print("⚠️ 저장된 데이터가 손상되어 있어 기본 퀴즈로 초기화합니다.")
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = None

    def save(self):
        """현재 퀴즈 목록과 최고 점수를 state.json에 저장한다."""
        data = {
            "quizzes": [
                {
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer,
                }
                for q in self.quizzes
            ],
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            print("⚠️ 저장 중 문제가 발생했습니다. (변경사항이 저장되지 않았을 수 있습니다)")

    # ── 메뉴 기능들 ──────────────────────────────────────

    def show_menu(self):
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

    def play_quiz(self):
        """퀴즈를 순서대로 출제하고, 정답 여부를 판정한 뒤 결과를 보여준다."""
        if not self.quizzes:
            print("😢 풀 수 있는 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        total = len(self.quizzes)
        print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")
        print("-" * 40)

        correct_count = 0

        for index, q in enumerate(self.quizzes, start=1):
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

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

        print("=" * 40)

        self.save()   # 점수가 바뀌었을 수 있으니 바로 저장

    def add_quiz(self):
        """새 퀴즈를 입력받아 self.quizzes에 추가한다."""
        print("📌 새로운 퀴즈를 추가합니다.")

        question = ask_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = ask_text(f"선택지 {i}: ")
            choices.append(choice)

        answer = ask_number("정답 번호 (1-4): ", 1, 4)

        new_quiz = Quiz(question=question, choices=choices, answer=answer)
        self.quizzes.append(new_quiz)

        print("✅ 퀴즈가 추가되었습니다!")

        self.save()   # 새 퀴즈가 사라지지 않도록 바로 저장

    def list_quizzes(self):
        """저장된 퀴즈 목록을 문제만 간단히 보여준다."""
        if not self.quizzes:
            print("📋 등록된 퀴즈가 없습니다.")
            return

        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for index, q in enumerate(self.quizzes, start=1):
            print(f"[{index}] {q.question}")

        print("-" * 40)

    def show_score(self):
        """지금까지의 최고 점수를 보여준다."""
        if self.best_score is None:
            print("😅 아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어보세요!")
            return

        print(f"🏆 최고 점수: {self.best_score}점")

    def run(self):
        """메뉴를 반복해서 보여주고, 사용자의 선택을 처리한다."""
        while True:
            self.show_menu()
            choice = ask_number("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save()
                print("👋 게임을 종료합니다. 안녕히 가세요!")
                break


def main():
    """프로그램 시작점. 강제 종료 상황에서도 안전하게 끝내도록 감싼다."""
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print()
        print("👋 지금까지의 내용을 저장하고 안전하게 종료합니다.")
        game.save()


if __name__ == "__main__":
    main()
