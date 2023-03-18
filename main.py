import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv('.env')


def send_email(message):
    sender: str = 'k.elfimow@gmail.com'
    password: str = os.getenv('PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Test'
        server.sendmail(sender, sender, msg.as_string())

        return 'OK'
    except Exception as ex:
        return '{}'.format(ex)


def main():
    message: str = input('Напишите своё сообщение: ')
    print(send_email(message))


if __name__ == '__main__':
    main()
