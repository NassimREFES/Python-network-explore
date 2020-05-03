import re
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

class SendMail(object):
    sonc = False
    ps = False
    m = MIMEMultipart()
    
    def __init__(self, from_, to_, subject="", message=""):
        self._from = self.correct_mail(from_)
        self._to = self.correct_mail(to_)
        self._sub = subject
        self._msg = message
        
    def correct_mail(self, mail):
        regex = re.compile(r"^[a-z0-9._-]+@[(hotmail|live|outlook|gmail)]+\.[(com|fr)]")
        if regex.match(mail) is  None:
            raise Exception(r'format de l adresse erronee')
        return mail
        
    def add_subject(self, sub2):
        self._sub = self._sub + sub2
        
    def add_message(self, msg2):
        self._msg = self._msg + '\n' + msg2
        
    def add_objet(self, _path):
        part = MIMEBase('application', 'octet_stream')
        part.set_payload(open(_path, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename='+_path)
        (self.m).attach(part)
    
    # par defaut
    def utilise_port_stl_ou_non_chiffre(self):
        self.sonc = True
    
    def utilise_port_ssl(self):
        self.ps = True
    
    def quel_smtp_utilise(self):
        for i in self._from.split('@'):
            d = i.split('.')
        x = ('hotmail', 'live', 'outlook', 'gmail')
        for i in x:
            if i in d:
                xx = i
        if xx == x[0] or xx == x[1] or xx == x[2] :
            return 'smtp.live.com'
        elif xx == x[3] : # donnée l'accée a partir du compte
            return 'smtp.gmail.com'
        else :   
            raise Exception('ne pas supporte')
        
    def envoyer(self, _user, _pass):
        self.m['From'] = self._from
        self.m['To'] = self._to
        self.m['Subject'] = self._sub
        (self.m).attach(MIMEText(self._msg))
        
        mailserver = smtplib.SMTP(self.quel_smtp_utilise(), 587)
        try:
            if self.ps : 
                mailserver = smtplib.SMTP(self.quel_smtp_utilise(), 465)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login(_user, _pass)
            mailserver.sendmail(_user, self._to, (self.m).as_string())
        finally:
            mailserver.quit()

  
a = SendMail('guepard_128@hotmail.fr', 'mohamedabbassa1@gmail.com', message='123456789')
#a.utilise_port_ssl()
a.add_message("987654321")
a.add_subject("loool")
a.add_objet("decorateur.py")
a.add_objet("fiche.py")
a.add_objet("1.png")
a.envoyer('guepard_128@hotmail.fr', '')
print a._from
print a._to
