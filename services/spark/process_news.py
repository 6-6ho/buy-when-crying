from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, to_date

# Spark 세션 생성
spark = SparkSession.builder \
    .appName("Process News Batch") \
    .getOrCreate()




# to-do


# Postgres 저장
summary.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/crypto_db") \
    .option("dbtable", "daily_news_summary") \
    .option("user", "user") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()

spark.stop()