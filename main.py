from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging

def test_excp():
    try:
        logging.info("An error occured")
        a= 1/0
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == "__main__":
    try:
        test_excp()
    except Exception as e:
        print(e)