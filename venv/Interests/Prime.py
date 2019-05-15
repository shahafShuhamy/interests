from httpClient.client import Get as ClientGet
from Utils.Logger import Logger
from Utils.XmlParser import XmlParser
import time

class Prime():
    nextUpdateTag = 'NextInterestDecisionDate'
    logger = None
    def __init__(self):
        self.logger = Logger()
        pass

    """
     this method returns an HTML with Table
     API return Table with no HTML Tags
    """
    def getPrime(self):
        self.log('getting prime interest...')
        baseUrl = "https://www.boi.org.il/he/BankingSupervision/Data/_layouts/boi/handlers/WebPartHandler.aspx"
        params = {'wp': 'ItemsAggregator', 'PageId': '150', 'CqfDateFrom': '', 'CqfDateTo': '',
              '_': '1557755447808'}
        params['CqfDateFrom'] = time.strftime("%d/%m/%Y")
        params['CqfDateTo'] = '01/01/'+time.strftime("%Y")
        self.log("Today : " + dateToday + ", First date of the Year " + startOfYear)
        # add html and body tags to make this an HTML.
        return "<html><body>" + ClientGet(baseUrl, params) + "</body></html>"

    """
    this method return a string with a date
    date is the next interests table will be updated
    """
    def getNextUpdate(self):
        self.log('getting next Update from xml...')
        xmlUrl = "https://www.boi.org.il/HE/BoiLatestPublication.xml"
        xmlParser = XmlParser()
        xmlResult = ClientGet(xmlUrl, None)
        value = xmlParser.findTagInString(xmlResult, self.nextUpdateTag)
        return value

    def log(self, message):
        self.logger.log('Prime', message)

    def TEST_Get_Next_Update(self):
        prime = Prime()
        print(prime.getNextUpdate())

    def TEST_Get_Prime_Table(self):
        prime = Prime()
        print(prime.getPrime())

# Unit Test for next_update method
# prime = Prime()
# prime.TEST_Get_Next_Update()

# Unit Tsst for get Prime
# prime = Prime()
# prime.TEST_Get_Next_Update()
