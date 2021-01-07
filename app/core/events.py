from typing import Callable
from multiprocessing import Process

from fastapi import FastAPI

from app.workers import detection


processes = []


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        process = Process(target=detection.run) 
        process.start()
        processes.append(process)
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    def stop_app() -> None:
        for process in processes:
            process.terminate()
    return stop_app
