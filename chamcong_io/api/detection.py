from typing import List
from pydantic import BaseModel

from .common import Response, Kafka


class DataConfig(BaseModel):
    consumer: Kafka
    producer: Kafka


class ResponseConfig(Response):
    data: List[DataConfig]