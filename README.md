# Apache Kafka Test

## Requerimientos
* Java 8
* Python 3

## Configurar Kafka
Descargar y descomprimir Apache Kafka versión [2.11-0.10.1.0](https://www.apache.org/dyn/closer.cgi?path=/kafka/0.10.1.0/kafka_2.11-0.10.1.0.tgz) desde el link otorgado.

* Correr Zookeeper
```bash
$ cd kafka_2.11-0.10.1.0
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

* Correr el servidor de Kafka

```bash
$ bin/kafka-server-start.sh config/server.properties
```

* Crear un `topic` para poder generar el `pub-sub` de mensajes.

```bash
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

## Configurar kafka-test

* Clonar este repositorio, y entrar a la carpeta principal.
```bash
$ cd kafka-test
```
* Editar en `Producer` el `host` por donde se publicara el sream de datos. Por default esta en localhost.
```python
def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')
```
Puedes poner más de un `host`, separandolos por coma.

* Correr desde la carpeta `kafka-test` el siguiente comando para ejecutar el microservicio.

```bash
$ python[3] Producer
```
_Si se tiene configurado Python 3 como default, correr solo `python`, en caso contrario, correr `python3`_

Se ejecutara en el puerto `5000` el productor. Este recibirá requests del tipo `POST`, de la forma:

```bash
[POST] http://127.00.1:5000/post/test?message="This is a text pusblished"
```

* Editar en `Consumer` el `host` de manera similar.

```python
def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')
```

* Correr desde la carpeta `kafka-test` el siguiente comando para ejecutar el microservicio.
```bash
$ python[3] Client
```
_Si se tiene configurado Python 3 como default, correr solo `python`, en caso contrario, correr `python3`_

Abrir en el navegador la dirección en el puerto `5001`. Se mostraran los mensajes recientes recibidor por el topic `test`.
