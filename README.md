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
- 외부 라이브러리 없음 (표준 라이브러리 `json`, `os`, `random`만 사용)

## 기능 목록

| 메뉴 | 기능 |
|---|---|
| 1 | 퀴즈 풀기 — 문제를 무작위 순서로 출제하고 채점, 최고 점수 갱신 |
| 2 | 퀴즈 추가 — 문제/선택지 4개/정답 입력받아 등록 후 저장 |
| 3 | 퀴즈 목록 — 등록된 문제를 등록 순서대로 요약 표시 |
| 4 | 점수 확인 — 최고 점수 표시 (기록이 없으면 안내) |
| 5 | 종료 — 저장 후 안전하게 종료 |

**입력 처리**
모든 숫자 입력은 앞뒤 공백 제거, 숫자 변환 실패, 허용 범위 밖, 빈 입력을 검사하고 재입력을 요청합니다.
`Ctrl+C`(KeyboardInterrupt) / `EOFError` 발생 시에도 비정상 종료 없이 저장 후 종료합니다.

**보너스 구현: 랜덤 출제**
`random.shuffle`로 퀴즈 풀기의 출제 순서를 매번 섞습니다.
`self.quizzes`를 직접 섞으면 목록(3번 메뉴)의 순서까지 바뀌므로, `.copy()`로 사본을 만들어 사본만 섞습니다.

## 파일 구조

```
my-quiz-game/
├── main.py                    # 프로그램 진입점 (Quiz, QuizGame 클래스 포함)
├── state.json                  # 퀴즈/최고점수 저장 파일 (실행 시 자동 생성)
├── .gitignore
├── README.md
└── docs/
    └── screenshots/             # 실행 화면 및 제출용 캡처
        ├── menu.png              # 메뉴 화면
        ├── play.png              # 퀴즈 풀기
        ├── add_quiz.png          # 퀴즈 추가
        ├── score.png             # 점수 확인
        ├── dev-environment.png   # 개발 환경 (Python/Git/VS Code 버전)
        ├── git-log.png           # git log --oneline --graph
        └── git-reflog.png        # clone / pull 실행 기록
```

## 데이터 파일 (state.json)

- 위치: 프로젝트 루트 (`./state.json`)
- 인코딩: UTF-8
- 역할: 등록된 퀴즈 목록과 최고 점수를 보관해, 프로그램을 재실행해도 데이터가 유지되게 합니다.
- 저장 시점: 퀴즈 추가 직후, 퀴즈 풀기 완료 직후, 프로그램 종료 시
- 파일이 없거나 손상된 경우, 안내 메시지를 출력하고 기본 퀴즈 5개로 자동 복구합니다.

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
| `question` | 문제 내용 (문자열) |
| `choices` | 선택지 4개 (문자열 배열) |
| `answer` | 정답 번호 (1~4) |
| `best_score` | 최고 점수(0~100). 아직 한 번도 풀지 않았으면 `null` |

## Git 작업 이력

- 기능 단위로 커밋을 나누어 진행했습니다. (`Feat`, `Fix`, `Docs`, `Refactor`, `Chore`)
- `feature/play-quiz`, `feature/random-order` 브랜치에서 기능을 개발한 뒤 `main`에 병합했습니다.
- 저장소를 별도 디렉터리에 `clone`하여 수정·`push`한 뒤, 기존 작업 디렉터리에서 `pull`로 반영했습니다.

## 실행 화면

| 화면 | 캡처 |
|---|---|
| 메뉴 | [menu.png](docs/screenshots/menu.png) |
| 퀴즈 풀기 | [play.png](docs/screenshots/play.png) |
| 퀴즈 추가 | [add_quiz.png](docs/screenshots/add_quiz.png) |
| 점수 확인 | [score.png](docs/screenshots/score.png) |
| 개발 환경 | [dev-environment.png](docs/screenshots/dev-environment.png) |
| Git 로그 | [git-log.png](docs/screenshots/git-log-oneline-graph.png) |
| Git clone/pull 기록 | [git-reflog.png](docs/screenshots/git-reflog.png) |
