import sys
import os
from pathlib import Path

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename =  exc_tb.tb_frame.f_code.co_filename
    filename = os.path.split(filename)[-1]
    
    error_message = f"Error occured in file name is [{filename}] in the line number is [{exc_tb.tb_lineno}] and the error message is [{str(error)}]"
    
    return error_message
    
class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
        
    def __str__(self):
        return self.error_message