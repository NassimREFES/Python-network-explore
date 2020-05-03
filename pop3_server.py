import getpass
import poplib

GOOGLE_POP3_SERVER = 'pop.mail.yahoo.com'#'pop-mail.outlook.com' #'pop.googlemail.com'
POP3_SERVER_PORT = '995'

def fetch_email(username, password):
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, POP3_SERVER_PORT)
    mailbox.user(username)
    mailbox.pass_(password)
    num_message = len(mailbox.list()[1])
    print('Total emails: {0}'.format(num_message))
    print('Getting last message')
    #f = open('mailmsg.txt', 'w')
    for i in range(num_message):
        for msg in mailbox.retr(i+1)[1]:
            #print(msg)
            msg = msg.decode('utf-8')
            #f.write(msg)
            if msg.find('Date') != -1:
                print (msg[msg.find('Date') : msg.find('Date') + 50])
    mailbox.quit()
    
if __name__ == '__main__':
    username = input('Enter your email user ID:')
    password = getpass.getpass(prompt='Enter your email password:')
    fetch_email(username, password)