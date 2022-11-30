from stt import Model
import numpy as np
from os.path import exists
import logManager as log
import file_handler as fh

centro = Model(fh.leggi_config()['model_filename'])


def traduci(arr: np.ndarray) -> str:
    return centro.stt(arr)


def setModel(path: str):
    global centro
    try:
        if exists(path):
            centro = Model(path)
    except FileExistsError:
        log.logError("File not found - model - path={" + path + "}")
        exit(0)
