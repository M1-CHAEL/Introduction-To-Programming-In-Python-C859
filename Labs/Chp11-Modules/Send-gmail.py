import smtplib
from email.mime.text import MIMEText

header = 'Hello. This is an automated email.\n\n'

def send(subject, to, frm, text):
    # The message to send
    msg = MIMEText(header + text)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = frm

    # Connect to gmail's email server and send
    s = smtplib.SMTP('smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(user=frm, password='password')
    s.sendmail(frm, [to], msg.as_string())
    s.quit()

if __name__ == "__main__":
    send(
        subject='A coupon for you!',
        to='billgates@microsoft.com',
        frm='JohnnysHotDogs1@gmail.com',
        text='Enjoy!')