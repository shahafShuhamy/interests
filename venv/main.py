from Interests.Prime import Prime
from Utils.Mailer import Mailer
from Utils.Logger import Logger
import time

def getPrimeInterest():
    primeGetter = Prime()
    primeInterest = primeGetter.getPrime()
    log("prime content: "+primeInterest)
    return primeInterest

def sendMail(content, htmlFlag, nextUpdateParam):
    mailer = Mailer()
    log('mailing to mailing list')
    mailer.sendMail(content, htmlFlag, nextUpdateParam)

def getNextUpdate():
    primeGetter = Prime()
    nextUpdate = primeGetter.getNextUpdate()

def main():
    try:
        primeTable = getPrimeInterest()
        nextUpdate = getNextUpdate()
        sendMail(primeTable, True, nextUpdate)
    except Exception as e:
        print(e)

def log(message):
    logger.log('Main',message)

logger = Logger()
if __name__ == "__main__":
    main()
