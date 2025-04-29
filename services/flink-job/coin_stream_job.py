from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env_settings = EnvironmentSettings.in_streaming_mode()
    t_env = StreamTableEnvironment.create(env, environment_settings=env_settings)

    # Kafka Source 등록
    t_env.execute_sql("""
    CREATE TABLE coin_ticks (
        coin STRING,
        price DOUBLE,
        ts TIMESTAMP(3),
        WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'coin-ticks',
        'properties.bootstrap.servers' = 'kafka:9092',
        'format' = 'json',
        'scan.startup.mode' = 'earliest-offset'
    )
    """)

    # PostgreSQL Sink 등록
    t_env.execute_sql("""
    CREATE TABLE coin_prices (
        coin STRING,
        price DOUBLE,
        ts TIMESTAMP(3)
    ) WITH (
        'connector' = 'jdbc',
        'url' = 'jdbc:postgresql://postgres:5432/crypto_db',
        'table-name' = 'coin_prices',
        'username' = 'user',
        'password' = 'password',
        'driver' = 'org.postgresql.Driver'
    )
    """)

    # 간단히 스트림 복사
    t_env.execute_sql("""
    INSERT INTO coin_prices
    SELECT coin, price, ts FROM coin_ticks
    """)

if __name__ == '__main__':
    main()
