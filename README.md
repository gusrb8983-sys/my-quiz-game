# 🐾 나만의 동물 퀴즈 게임

터미널에서 실행되는 4지선다 동물 퀴즈 게임입니다.
Python 기본 문법과 클래스, JSON 파일 저장을 사용해 만들었습니다.

## 개요

- `Quiz` 클래스로 문제 하나하나를, `QuizGame` 클래스로 게임 전체(퀴즈 목록·최고 점수·메뉴 진행)를 관리합니다.
- 퀴즈와 최고 점수는 `state.json`에 저장되어, 프로그램을 껐다 켜도 유지됩니다.

## 퀴즈 주제: 동물

동물을 좋아해서 골랐고, 문제/선택지/정답을 직접 만들기 쉬운 주제라 입문 미션에 적합하다고 판단했습니다.

## 실행 방법

```bash
git clone https://github.com/gusrb8983-sys/my-quiz-game.git
cd my-quiz-game
python3 main.py
```

- Python 3.10 이상 필요
- 외부 라이브러리 없음 (표준 라이브러리만 사용)

## 기능 목록

| 메뉴 | 기능 |
|---|---|
| 1 | 퀴즈 풀기 — 문제를 순서대로 출제하고 채점, 최고 점수 갱신 |
| 2 | 퀴즈 추가 — 문제/선택지 4개/정답 입력받아 등록 |
| 3 | 퀴즈 목록 — 등록된 문제를 요약해서 표시 |
| 4 | 점수 확인 — 최고 점수 표시 |
| 5 | 종료 — 저장 후 안전하게 종료 |

모든 숫자 입력은 공백 제거, 숫자 변환 실패, 범위 밖 입력, 빈 입력을 검사합니다.
`Ctrl+C` / `EOFError` 발생 시에도 비정상 종료 없이 저장 후 종료합니다.

## 파일 구조

```
my-quiz-game/
├── main.py               # 프로그램 진입점 (Quiz, QuizGame 클래스 포함)
├── state.json             # 퀴즈/최고점수 저장 파일 (실행 시 자동 생성)
├── .gitignore
├── README.md
└── docs/
    └── screenshots/        # 실행 화면 캡처
        ├── menu.png
        ├── play.png
        ├── add_quiz.png
        └── score.png
```

## 데이터 파일 (state.json)

- 위치: 프로젝트 루트 (`./state.json`)
- 인코딩: UTF-8
- 파일이 없거나 손상된 경우, 기본 퀴즈 5개로 자동 복구합니다.

```json
{
  "quizzes": [
    {
      "question": "문제 내용",
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
      "answer": 1
    }
  ],
  "best_score": 80
}
```

| 필드 | 설명 |
|---|---|
| `quizzes` | 등록된 퀴즈 목록 (`question`, `choices`, `answer`) |
| `answer` | 정답 번호 (1~4) |
| `best_score` | 최고 점수. 아직 한 번도 안 풀었으면 `null` |

## 실행 화면

- [메뉴 화면](docs/screenshots/menu.png)
- [퀴즈 풀기](docs/screenshots/play.png)
- [퀴즈 추가](docs/screenshots/add_quiz.png)
- [점수 확인](docs/screenshots/score.png)

> 이 줄은 clone/pull 실습을 위해 추가되었습니다.
