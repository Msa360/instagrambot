# emails for receiving insights
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os_info import getAvailableSpace
import os

load_dotenv()
sender = 'arnaud25juin@gmail.com'
receivers = ['arnaud25@icloud.com']
 

html_msg = f'''
    <html>
        <body>
            <h3>Weekly Insights</h3>
            <p><h5>Space left on machhine: </h5>{getAvailableSpace()}</p>
        </body>
    </html>
    '''
email_msg = MIMEMultipart()
email_msg['From'] = 'Whale Project {-}'
email_msg['To'] = 'arnaud25@icloud.com'
email_msg['Subject'] = 'Whale Project\'s weekly'
email_msg.attach(MIMEText(html_msg, 'html'))
email_msg_str = email_msg.as_string()


def send_mail(sender=sender, receiverslist=receivers, message=email_msg_str):
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.login(os.getenv("MAIL"), os.getenv("MAILPASSWORD"))
    smtpObj.sendmail(sender, receiverslist, message)         
    print("Successfully sent email")
    smtpObj.quit()


# send_mail()