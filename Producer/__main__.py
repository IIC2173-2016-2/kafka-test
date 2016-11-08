import json as j
from pykafka import KafkaClient
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


@app.route('/topics/')
def topics():
    client = get_kafka_client()
    return jsonify([topic for topic in client.topics])


@app.route('/post/<topic>', methods=['POST'])
def write_to_topic(topic):
    message = request.args.get('message', '')
    client = get_kafka_client()
    topic = client.topics[topic.encode('ascii')]
    producer = topic.get_sync_producer()
    producer.produce(str.encode(message))
    return "OK"


@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()


def events():
    for i in client.topics[topicname.encode('ascii')].get_simple_consumer():
        yield 'data: {0}\n\n'.format(i.value)
    return Response(events(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run()
