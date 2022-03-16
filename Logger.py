import logging
import datetime
import os
import sys


class LogFile:
    def __init__(self, log_state):
        if log_state:
            stamp = datetime.datetime.now()
            if sys.platform == "win32" or sys.platform == "win64":
                log_file_name = f'RunTime{stamp.hour}{stamp.minute}{stamp.second}.log'
            else:
                log_file_name = f'RunTime_{stamp.hour}:{stamp.minute}:{stamp.second}.log'
            log_directory_name = 'Logs'
            LogFile.__create_log_file(log_directory_name, log_file_name)
            logging.info("Log file configured!")

    @staticmethod
    def log_message(msg, state):
        if state == "info":
            logging.info(msg)
        if state == "debug":
            logging.debug(msg)
        if state == "error":
            logging.error(msg)

    @staticmethod
    def __create_log_file(directory, file):
        if not os.path.isdir(directory):
            os.mkdir(directory)
        if sys.platform == "win32" or sys.platform == "win64":
            logging.basicConfig(filename=f"{os.getcwd()}/{directory}/{file}", format='%(levelname)s - %(message)s',
                                level=logging.INFO)
        else:
            logging.basicConfig(filename=f"{directory}/{file}", format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.INFO, datefmt='%H:%M:%S:%s')
