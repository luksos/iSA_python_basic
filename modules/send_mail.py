
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def wyslij_mail(temat, tresc):
    """
    Funkcaj która wysła maila o określonym temacie i treści do "isapy@o2.pl"
    """

    mail = MIMEMultipart()
    mail["Subject"] = temat
    mail["To"] = 'isapy@o2.pl'
    mail["From"] = 'isapy@int.pl'

    body = MIMEText(tresc)
    mail.attach(body)

    server = smtplib.SMTP('poczta.int.pl')
    server.login('isapy@int.pl', 'isapython;')
    server.send_message(mail)
    server.quit()

    print("Wysłano mail!")
