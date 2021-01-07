import time
import pickle
import requests
from typing import List
from multiprocessing import Process

# import cv2
from kafka import KafkaProducer, KafkaConsumer

from chamcong_io.api.detection import ResponseConfig, DataConfig
from chamcong_io.api.common import Kafka as KafkaIo
from app.core.config import REGISTRY_API
from app.core.config import DETECTION_ALIGN


def get_config() -> List[DataConfig]:
    try:
        response = requests.get(REGISTRY_API, timeout=10)
        if response.status_code == 200:
            response_config = response.json()
            config = ResponseConfig(status=response_config["status"], message=response_config["message"], data=response_config["data"])
            return config.data
        else:
            raise Exception(f"request registry failed, status:{response.status_code}")
    except Exception as e:
        raise Exception(f"{e}")    
    

def run():
    try:
        config = get_config()
        processess = []
        for data in config:
            consume = data.consumer
            produce = data.producer
            process = Process(target=detect, args=(consume, produce))
            processess.append(process)
        # start process
        for process in processess:
            process.daemon=True
            process.start()
        # join process
        for process in processess:
            process.join()
    except Exception as e:
        print(e)
        

def detect(consume, produce):
    try:
        # kafka producer
        kafka_producer = KafkaProducer(
            value_serializer=lambda m:pickle.dumps(m),
			key_serializer=lambda m:pickle.dumps(m),
			bootstrap_servers=produce.brokers
        )
        # kafka consumer
        kafka_consumer = KafkaConsumer(
            consume.topic,
            group_id=consume.group_id,
            value_deserializer=lambda m:pickle.loads(m),
			key_deserializer=lambda m:pickle.loads(m),
            bootstrap_servers=consume.brokers,
        )
        # detection
        for message in kafka_consumer:
            print(message.topic)
    except Exception as e:
        print(e)
