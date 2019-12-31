from Interests.Prime import Prime
from Utils.Logger import Logger
from Utils.Mailer import Mailer
import time

def getPrimeInterest():
    primeGetter = Prime()
    primeInterest = primeGetter.getPrime()
    log(primeInterest)
    return primeInterest

def sendMail(content, htmlFlag, nextUpdateParam):
    mailer = Mailer()
    log('mailing to mailing list')
    mailer.sendMail(content, htmlFlag, nextUpdateParam)

def getNextUpdate(primeTable):
    primeGetter = Prime()
    nextUpdate = primeGetter.getNextUpdate(primeTable)
    return nextUpdate

def main():
    try:
        primeTable = getPrimeInterest()
        nextUpdateToMail = getNextUpdate(primeTable)
        sendMail(primeTable, True, nextUpdateToMail)
    except Exception as e:
        print(e)

def log(message):
    logger.log('Main',message)

logger = Logger()
if __name__ == "__main__":
    main()
