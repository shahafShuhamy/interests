import time
class Logger():
    def __init__(self):
        pass
    def log(self, context, message):
        print('['+context+' - log] '+ time.strftime("%c") + ': '+ message)