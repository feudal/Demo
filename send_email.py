from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height,count):
    from_email="calmis87@gmail.com"
    from_password="xiaomimia1"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. The average height of all is <strong>%s</strong>.\
     and that is calculated out %s of people" % (height,avg_height,count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
