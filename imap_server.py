import getpass
import imaplib
import pprint

GOOGLE_IMAP_SERVER = 'imap-mail.outlook.com'#'imap.googlemail.com'
IMAP_SERVER_PORT = '993'

def check_email(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, IMAP_SERVER_PORT)
    mailbox.login(username, password)
    mailbox.select('Sent')
    tmp, data = mailbox.search(None, 'ALL')
    #f = open('imapmail.txt', 'w')
    for num in data[0].split():
        tmp, data = mailbox.fetch(num, '(RFC822)')
        print('Message: {0}\n'.format(num))
        raw_email = data[0][1]
        raw_email = raw_email.decode('utf-8')
        print(raw_email[raw_email.find('Date'):raw_email.find('Date')+50])
        #pprint.pprint(data[0][1])
        #f.write(raw_email)
        #f.write('\n\n\n\n')
        #break;
        
    mailbox.close()
    mailbox.logout()
    
if __name__ == '__main__':
    username = input('Enter your email username:')
    password = getpass.getpass(prompt='Enter your account password:')
    check_email(username, password)
    