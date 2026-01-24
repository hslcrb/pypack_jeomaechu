# 점메추 (jeomaechu)

결정 장애가 있는 분들을 위한 전문적인 점심 메뉴 추천 파이썬 패키지입니다. "오늘 점심 뭐 먹지?"라는 고민을 한 방에 해결해 드립니다.

## 주요 기능
- **최적화된 성능**: 데이터셋 캐싱을 통해 즉각적인 추천이 가능합니다.
- **가장 쉬운 사용법**: 인자 없이 `jeomaechu`만 입력해도 즉시 추천을 시작합니다.
- **방대한 데이터베이스**: 프랜차이즈 상호명을 포함한 500개 이상의 메뉴 수록.
- **깔끔한 파이썬 API**: 개발자가 쓰기 편하도록 직관적인 메서드를 제공합니다.

## 설치 방법
```bash
pip install .
```

## 사용 방법 (CLI)
명령어가 훨씬 짧고 강력해졌습니다:

```bash
# 그냥 실행하세요! (즉시 랜덤 추천)
jeomaechu

# 메뉴 추천 받기 (상세 옵션 사용 시)
jeomaechu pick

# 여러 개 동시에 추천 받기
jeomaechu pick -n 5

# 카테고리나 태그 지정
jeomaechu pick -c "Korean (한식)"
jeomaechu pick -t "Spicy (매콤)"

# 데이터 탐색
jeomaechu cats    # 카테고리 목록 보기
jeomaechu tags    # 태그 목록 보기
jeomaechu all     # 모든 메뉴 데이터 보기
```

## 파이썬 API 사용법
API가 성능과 가독성 면에서 최적화되었습니다:

```python
from jeomaechu import JeomMaeChu

engine = JeomMaeChu()

# 단일 랜덤 추천
cat, menu = engine.recommend_random()

# 다중 랜덤 추천 (고성능 샘플링)
results = engine.recommend_many(5)
```

## 라이선스
MIT
