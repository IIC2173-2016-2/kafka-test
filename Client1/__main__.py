from pykafka import KafkaClient
from flask import Flask, jsonify, render_template, Response


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()
    topic = client.topics[topicname.encode('ascii')]
    # for i in topic.get_simple_consumer():
    #     print("Message: ", str(i.value))
    #     return make_response(i.value(), mimetype="text/event-stream")
    def events():
        for i in client.topics[topicname.encode('ascii')].get_simple_consumer():
            yield 'data: {0}\n\n'.format(i.value)
    return Response(events(), mimetype="text/event-stream")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)
