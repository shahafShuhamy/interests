from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Utils.Logger import Logger
import smtplib

class Mailer():
    server = None
    message = ""
    emails = ["email"]
    logger = Logger()

    def __init__(self):
        pass

    def sendMail(self, message ,htmlFlag, nextUpdateParam):
        if(htmlFlag):
            self.message = MIMEMultipart(
                "alternative", None, [MIMEText(message), MIMEText(message, 'html')])
        else:
            self.message = MIMEText(message)
        self.message['Subject'] = 'Prime Interest For this Month, Next Update At '+nextUpdateParam
        self.message['From'] = 'PrimeService - Auto Generated'
        self.message['To'] = self.emails
        self.server = smtplib.SMTP('smtp.gmail.com', 587, "email", timeout=120)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login('email', 'password')
        self.server.sendmail("emailFrom", self.emails, self.message.as_string())
        self.server.close()
        pass

    def log(self, message):
        self.logger.log('Mailer', message)