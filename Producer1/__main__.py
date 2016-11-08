import json as j
from pykafka import KafkaClient
from flask import Flask, jsonify, render_template, Response, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)


class MessageForm(Form):
    message = TextAreaField('Mensaje', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def home():
    form = MessageForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        mensaje = request.form['message']
        print(mensaje)
        if form.validate():
            # Save the comment here.
            return redirect(url_for('write_to_topic',
                                    topic='test',
                                    message="'{}'".format(mensaje)),
                            code=307)
        else:
            print("Nope")

    return render_template('home.html', form=form)


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
    return render_template('index.html')


@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', form=form)

if __name__ == "__main__":
    app.run(port=5003)
