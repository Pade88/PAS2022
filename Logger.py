import logging
import datetime
import os


class LogFile:
    def __init__(self, log_state):
        if log_state:
            stamp = datetime.datetime.now()
            log_file_name = 'RunTime_{}:{}:{}.log'.format(stamp.hour, stamp.minute, stamp.second)
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

        logging.basicConfig(filename="{}/{}".format(directory, file), format='%(asctime)s - %(levelname)s - %(message)s',
                            level=logging.INFO, datefmt='%H:%M:%S:%s')
