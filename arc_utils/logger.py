import logging
from logging.handlers import TimedRotatingFileHandler


class Logger():
    def __init__(self,file_path,when="h",interval=1,backupCount=48,key=__name__):
        self.logger = logging.getLogger(key)
        self.logger.setLevel(logging.INFO)
        formatter=logging.Formatter('{ "time" : "%(asctime)s" , "level" : "%(levelname)s" ,  "message" : "%(message)s"}')
        handler = TimedRotatingFileHandler(file_path, #log file path
                                        when=when, # h = hour
                                        interval=interval, #rotate file after every hour
                                        backupCount=backupCount)  #overwrite first file after 48 hours (interval * 48)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def getLogger(self):
        return self.logger
