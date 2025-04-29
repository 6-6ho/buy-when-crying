#!/bin/bash

# Kafka 서버가 완전히 뜰 때까지 잠시 대기
sleep 10

# 토픽 생성 (원하는 토픽 명 수정 가능)
kafka-topics.sh --create --topic coin-ticks --bootstrap-server kafka:9092 --partitions 3 --replication-factor 1
kafka-topics.sh --create --topic news-headlines --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1

# 상태 출력
kafka-topics.sh --list --bootstrap-server kafka:9092

# 컨테이너 유지
tail -f /dev/null
