import logging
from logging.handlers import TimedRotatingFileHandler


class FilebeatLog():
    def __init__(self,file_path):
        self.logger = logging.getLogger("Rotating Log")
        self.logger.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = TimedRotatingFileHandler(file_path, #log file path
                                        when="h", # h = hour
                                        interval=1, #rotate file after every hour
                                        backupCount=48)  #overwite first file after 48 hours (interval * 48)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def getLogger(self):
        return self.logger

    # def info(self,msg):
    #     self.logger.info(msg)

    # def warn(self,msg):
    #     self.logger.warn(msg)

    # def error(self,msg):
    #     self.logger.error(msg)
