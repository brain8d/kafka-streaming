services:
  zookeeper:
    image: zookeeper:latest
    ports:
     - "2181:2181"
  kafka:
    image: apache/kafka:latest
    ports:
     - "9092:9092"
    expose:
     - "9093"
    environment:
      KAFKA_ADVERTISED_LISTENERS: INSIDE://kafka:9093,OUTSIDE://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
      KAFKA_LISTENERS: INSIDE://0.0.0.0:9093,OUTSIDE://0.0.0.0:9092
      KAFKA_INTER_BROKER_LISTENER_NAME: INSIDE
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_CREATE_TOPICS: "topic_test:1:1"
    volumes:
     - /var/run/docker.sock:/var/run/docker.sock 



# # Docker image kafka
docker run -p 9092:9092 --name kafka-server apache/kafka:3.7.0

# Set up kafka topic directly from docker
docker exec -it kafka-server /opt/kafka/bin/kafka-topics.sh --create --topic delhaize-shop --bootstrap-server localhost:9092

# Or from bash
kafka-topics.sh --create --topic delhaize-shop --bootstrap-server localhost:9092

# or run bash
docker exec -it kafka-server bash # then run commands in /opt/kafka/bin/

# check if file is created
kafka-topics.sh --list --bootstrap-server localhost:9092

kafka-topics.sh --describe --topic delhaize-shop --bootstrap-server localhost:9092

# KAFKA producer
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic # topic name first_topic

# Kafka consume messages in console
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic delhaize-shop

# Launch API 

uvicorn api.api:app --host 0.0.0.0 --port 8000 

# add opt/kafka/bin to path , makes testing easier
export KAFKA_HOME=/opt/kafka/bin
export PATH=$KAFKA_HOME:$PATH


## login details for POSTGRES DB ON AWS

- DB identifier = kafka-db-instance
- databse name = kafka-database
- username = root
- pass = root1234
- port = 5432


# AWS
aws audrey db username: brian
aws audrey db pass : brian1234@

#
export RDSHOST="database-1.czkwus82o4b9.us-east-1.rds.amazonaws.com"
export PGPASSWORD="$(aws rds generate-db-auth-token --hostname $RDSHOST --port 5432 --region us-east-1 --username brian)"
echo $PGPASSWORD


psql -h database-1.czkwus82o4b9.us-east-1.rds.amazonaws.com -p 5432 "dbname=mydatabase user=brian"
pgcli -h database-1.czkwus82o4b9.us-east-1.rds.amazonaws.com -p 5432 -u brian -d mydatabase