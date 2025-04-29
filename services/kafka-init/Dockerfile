FROM wurstmeister/kafka

COPY create-topics.sh /create-topics.sh
RUN chmod +x /create-topics.sh

CMD ["/create-topics.sh"]
