import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'localhost'
smtp_port = 25

sender = 'toni.culic1@gmail.com'
receiver = 'anteprojic@gmail.com'
subject = 'Testna poruka'
message = 'Ovo je testna poruka poslana pomoću Pythona i lokalnog SMTP servera.'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

smtp_obj.send_message(msg)

smtp_obj.quit()
