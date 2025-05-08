## 프로젝트 소개

`buy-when-crying`는 시장 심리가 두려움이나 무관심으로 기울 때를 감지하고, 이를 투자 타점 판단에 참고할 수 있도록 신호 형태로 제공하는 데이터 파이프라인입니다.
시장 참여자의 심리 변화를 정량적으로 분석하여, 과도한 공포나 관심 저하 국면을 포착하는 데 초점을 맞추고 있습니다.
---

## 💡 프로젝트 개요

Kafka, Flink, NiFi, PostgreSQL, FastAPI, Airflow 등을 사용한 데이터 처리 환경을 구성했습니다.

- **코인 실시간 데이터**는 Kafka → Flink → PostgreSQL 로 처리
- **뉴스/경제지표** 데이터는 추후 배치 DAG로 Airflow에 연동 예정
- Apache NiFi는 데이터 흐름을 직관적으로 확인하거나 샘플 처리용으로 사용

---

## 🧩 구성 요소 및 기술

| 역할             | 기술 스택         |
|------------------|------------------|
| 스트리밍 처리     | Kafka, Flink     |
| 배치 처리         | Spark, Airflow   |
| 데이터 흐름 관리 | Apache NiFi      |
| 데이터 저장소     | PostgreSQL       |
| API 서버         | FastAPI          |

---

## 🖥️ 주요 포트 정리

| 포트 번호 | 서비스        | 비고                                |
|-----------|----------------|-------------------------------------|
| 9092      | Kafka          | 브로커                              |
| 8080      | Spark Master   | 웹 UI                               |
| 8081      | Spark Worker 1 |                                     |
| 8082      | Spark Worker 2 |                                     |
| 8083      | Flink          | Flink JobManager UI                 |
| 8084      | NiFi           | HTTPS 기본 포트 (`https://localhost:8443/nifi`) |
| 8085      | Airflow        | Web UI                              |
| 5432      | PostgreSQL     | DB 연결용                           |
| 8000      | FastAPI        | API 서버 (요청 처리용)              |

---

## 🛠 작업 완료 내역

- ✅ Kafka 토픽 생성 (coin-ticks, news-headlines)
- ✅ Binance WebSocket 기반 Kafka Producer 구현
- ✅ Flink Stream Job 작성 (Kafka → PostgreSQL)
- ✅ Docker Compose로 전체 환경 구성
- ✅ Nifi HTTPS 기반 인증 설정 완료 (개발용으로 간소화 가능)

---

## 📌 앞으로 할 일

- [ ] 뉴스/경제지표 배치 DAG 구성 (Airflow)
- [ ] PostgreSQL 테이블 구조 최적화
- [ ] 대시보드 연동 (Optional)

