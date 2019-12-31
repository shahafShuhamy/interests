import xml.etree.ElementTree as ET
import programUtils.Logger as Logger

class XmlParser():
    logger = None
    def __init__(self):
        self.logger = Logger()
        pass

    def findTagInString(self, str, whatToSearch):
        self.log('searching for tag: ' + whatToSearch +'in the string: \n' + str)
        root = ET.fromstring(str)
        tag = root.find('.//'+whatToSearch)
        return tag.text

    def log(self, message):
        self.logger.log('XML Parser', message)

    def TEST_read_from_file(self):
        root = ET.parse('TestFile.xml')
        tag = root.find('.//tag1')
        print(tag.text)

    def TEST_read_from_string(self):
        root = ET.fromstring("<root><tag2>Val2</tag2><tag>val1</tag></root>")
        tag = root.find('.//tag2')
        print(tag.text)