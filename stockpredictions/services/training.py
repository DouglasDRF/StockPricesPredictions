import numpy as np
import matplotlib.pyplot as plt

from stockpredictions.core.consts import PredictionType, Direction
from stockpredictions.models import TrainingLog
from stockpredictions.core.model import get_model_instance 
from stockpredictions.core.data_helper import load_dataset
from stockpredictions.data import TrainingLogRepository
import datetime as dt
import threading


class TrainingService:

    def __init__(self):
        self.__training_log = TrainingLogRepository()
        self.__model = get_model_instance()

    def train(self, ticker: str):
        t = threading.Thread(target=self.__train_task, args=(ticker,), daemon=True)
        t.start()
        return { "status_message": "train task has been scheduled"}

    def get_status(self):
        # return { "is_model_trained": self.__model.is_trained, "current_accuracy": self.__model.current_accuracy }
        return { "is_model_trained": self.__model.is_trained }

    def __train_task(self, ticker):
        try:
            dataset = load_dataset(ticker)
            model_saved = self.__model.train(dataset, True)
            self.__training_log.save_training_log(TrainingLog(dt.datetime.now().isoformat(), len(dataset), float(self.__model.current_accuracy), model_saved))
            print("Train task ran sucessfully")
        except Exception as e:
            print("Train task ran with error: \n" + str(e))


    