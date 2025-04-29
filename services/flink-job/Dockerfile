FROM apache/flink:1.16-scala_2.12-java11

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY coin_stream_job.py /app/coin_stream_job.py

ENTRYPOINT ["python", "/app/coin_stream_job.py"]
