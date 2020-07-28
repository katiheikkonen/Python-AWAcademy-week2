from crontab import CronTab
import requests
import smtplib

#  SEND MAIL
def send_mail(email, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, password)

    msg = "\nError!"
    server.sendmail(email, "katzuh@gmail.com", msg)

#  AUTOMATE SENDING MAIL
def automatization(automatize):
    times = 0
    if times < 5:
        cron = CronTab(user='ec2-user')
        job = cron.new(command=automatize)
        job.second.every(15)
        times += 1
        cron.write()

#  HEALTH CHECK
def health_check(checked_item):
    status = requests.get(checked_item)
    return status.status_code

check_healt = health_check('http://www.gmail.com')

if check_healt != 200:
    automatization(send_mail("tsttestitesti@gmail.com", "testitesti12"))
else:
    print('OK')
