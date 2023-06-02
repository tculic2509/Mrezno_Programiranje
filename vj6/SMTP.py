import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Postavite podatke za lokalni SMTP server
smtp_server = 'localhost'
smtp_port = 25

# Postavite podatke za e-mail
sender = 'toni.culic1@gmail.com'
receiver = 'anteprojic@gmail.com'
subject = 'Testna poruka'
message = 'Ovo je testna poruka poslana pomoću Pythona i lokalnog SMTP servera.'

# Stvorite MIME poruku
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Stvorite SMTP objekt i povežite se s lokalnim SMTP serverom
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

# Pošaljite e-mail
smtp_obj.send_message(msg)

# Odspojite se od SMTP servera
smtp_obj.quit()
