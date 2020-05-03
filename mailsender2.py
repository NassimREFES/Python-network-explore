import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 # 465 for ssl, 587 for tls

def send_email(sender, recipient):  
    """ send email message """
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    msg['Subject'] = input('Enter your email subject:\n> ')
    message = input('Enter your email message. Press Enter when finished.\n> ')
    part = MIMEText('', '')
    part.set_payload(message)
    msg.attach(part)
    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.set_debuglevel(1)
    session.ehlo()
    session.starttls()
    session.ehlo()
    pwd = getpass.getpass(prompt='Enter your email password:\n> ')
    # login to server
    session.login(sender, pwd)
    # send email
    session.sendmail(sender, recipient, msg.as_string())
    print('You email is sent to {0}.'.format(recipient))
    session.quit()
    
if __name__ == '__main__':
    sender = input('Enter sender email address:\n> ')
    recipient = input('Enter recipient email address:\n> ')
    send_email(sender, recipient)
