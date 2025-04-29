# buy-when-crying

A data pipeline that monitors and indicates when market sentiment turns fearful or disinterested.

---

## 프로젝트 소개

`buy-when-crying`는 시장 참가자들의 관심 저하 또는 불안 심리를 감지하고, 이를 지표 형태로 제공하는 데이터 수집 및 분석 시스템입니다.  
"남들이 울 때 산다"는 투자 격언을 모티브로, 시장 냉각 시점을 빠르게 파악할 수 있도록 설계되었습니다.

---

## 시스템 아키텍처

- Zookeeper + Kafka: 실시간 스트리밍 메시지 큐
- Flink: 코인 시세 실시간 처리
- Spark: 뉴스 데이터 배치 처리
- Apache NiFi: 실시간 데이터 흐름 시각화
- PostgreSQL: 데이터 저장소
- FastAPI: 데이터 조회용 API 서버
- Airflow: 전체 잡 스케줄링 및 관리

---

## 기술 스택

| 구성 요소 | 사용 기술 |
|:----------|:----------|
| 스트리밍 처리 | Kafka, Flink |
| 배치 처리 | Spark, Airflow |
| 데이터 흐름 관리 | Apache NiFi |
| 데이터 저장소 | PostgreSQL |
| API 서버 | FastAPI |

---