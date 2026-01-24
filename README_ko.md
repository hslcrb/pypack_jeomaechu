# 점메추 (jeomaechu) 🍱

파이썬을 위한 방대하고 전문적인 점심 메뉴 추천 엔진입니다. "오늘 점심 뭐 먹지?"라는 인류 최대의 난제를 해결해 드립니다. 정통 세계 요리부터 극사실주의 현실 집밥까지 600개 이상의 큐레이션된 데이터를 제공합니다.

---

## 🚀 주요 기능

- **방대한 데이터베이스**: 666개 이상의 엄선된 메뉴 아이템 수록.
- **100% 태그 시스템**: 모든 아이템이 맛, 식재료, 스타일별로 분류되어 있습니다.
- **하이퍼 리얼리즘**: "김자반에 밥 비벼먹기", "라면 국물에 찬밥 말기" 등 현실적인 끼니 포함.
- **글로벌 원어 명칭**: 어설픈 번역 대신 현지 발음 및 정통 명칭 사용 (예: *톤토로동*, *뻬스카토레*, *마라시앙궈*).
- **초고속 엔진**: 데이터 캐싱 최적화로 대량의 추천도 즉각 수행.
- **미려한 CLI**: `rich` 라이브러리를 활용한 감각적인 터미널 출력.

---

## 🛠 설치 방법

```bash
pip install .
```

---

## 💻 사용 방법 (CLI)

사용자 편의를 최우선으로 설계된 명령어 세트입니다.

### 🎲 즉시 추천 (기본)
아무 인자 없이 명령어만 입력하면 즉시 운명의 메뉴가 결정됩니다.
```bash
jeomaechu
```

### 🎯 조건부 추천 (Pick)
`pick` 명령어를 통해 상세한 조건을 지정할 수 있습니다.

| 옵션명 | 짧은 이름 | 설명 | 실행 예시 |
| :--- | :--- | :--- | :--- |
| `--count` | `-n` | 추천받을 메뉴의 개수 | `jeomaechu pick -n 5` |
| `--category`| `-c` | 특정 카테고리 내에서 선택 | `jeomaechu pick -c "Korean (한식)"` |
| `--tag` | `-t` | 특정 태그(기분/재료)로 필터링 | `jeomaechu pick -t "Spicy (매콤)"` |

**복합 사용 예시:**
```bash
# 매콤한 해산물 메뉴 중 3가지 추천 받기
jeomaechu pick -t "Seafood (해산물)" -t "Spicy (매콤)" -n 3
```

### 🔍 데이터 탐색
방대한 메뉴판을 직접 살펴보세요.
- `jeomaechu cats`: 사용 가능한 모든 음식 카테고리 목록 보기.
- `jeomaechu tags`: 맛, 재료, 분위기별 태그 목록 보기.
- `jeomaechu all`: 데이터베이스 내의 **모든** 메뉴를 표 형태로 보기.

### ⚡ 단축 명령어 (초고속 사용)
더욱 빠른 추천을 위해 단축 명령어를 지원합니다.

| 풀 네임 | 단축키 | 필터 단축키 | 실행 예시 |
| :--- | :--- | :--- | :--- |
| `jeomaechu` | `j` | - | `j` |
| `pick` | `p` | - | `j p -n 5` |
| `cats` | `c` | - | `j c` |
| `tags` | `t` | - | `j t` |
| `all` | `a` | - | `j a` |

**카테고리 단축어:**
`-c` 옵션 뒤에 한 글자만 입력해도 해당 카테고리를 인식합니다:
- `한`: 한식
- `중`: 중식
- `일`: 일식
- `양`: 양식
- `집`: 찐 집밥/현실
- `아`: 아시아/기타
- `상`: 상호명 (프랜차이즈)

**실행 예시:** `j p -c 한` (한식 메뉴 랜덤 추천)

---

## 🐍 파이썬 API 사용법

자신의 프로젝트에 추천 엔진을 간단히 통합할 수 있습니다.

```python
from jeomaechu import JeomMaeChu

# 최적화된 엔진 초기화
engine = JeomMaeChu()

# 단일 랜덤 추천 (카테고리, 메뉴명 반환)
cat, menu = engine.recommend_random()
print(f"오늘 점심은 {cat}의 '{menu}' 어떠세요?")

# 필터를 사용한 다중 추천
# List[Tuple[Optional[Category], Menu]] 형식 반환
picks = engine.recommend_many(count=10, tag="Spicy (매콤)")

# 전체 데이터 조회
all_menus = engine.get_all_menus()
categories = engine.get_categories()
```

---

## 📑 관련 문서
- [English README](README.md)
- [기여 방법 (Contributing)](CONTRIBUTING_ko.md)
- [라이선스 (License)](LICENSE)
- [주의사항 (Notice)](NOTICE_ko.md)

---

## ⚖️ 라이선스
MIT License. 상세 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
