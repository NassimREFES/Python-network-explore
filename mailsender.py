import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'aspmx.l.google.com'
SMTP_PORT = 25

def send_email(sender, recipient):
    """ send email message """
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Entrer your email subject: ')
    msg['Subject'] = subject
    message = input('Enter your email message. Press Enter when finished. ')
    part = MIMEText('', '')
    part.set_payload(message)
    msg.attach(part)
    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.set_debuglevel(1)
    # send Mail
    session.sendmail(sender, recipient, msg.as_string())
    print('You email is sent to {0}.'.format(recipient))
    session.quit()
    
if __name__ == '__main__':
    sender = input('Enter sender email address:')
    recipient = input('Enter recipient email address:')
    send_email(sender, recipient)