import logging
import src.logger  #the logger.py is imported so that it can get logged in the logs
import sys   #any exception getting control the sys library will automatically have that information   (sys is a run time related library)
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error has occured in python script name [{0}] at line [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_obj,error_detail:sys):
        super().__init__(error_obj)
        self.error_message=error_message_details(error_obj,error_detail)

    def __str__(self):
        return self.error_message
