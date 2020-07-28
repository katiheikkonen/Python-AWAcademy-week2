import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("tsttestitesti@gmail.com", "testitesti12")

msg = "\nHello World!"
server.sendmail("tsttestitesti@gmail.com", "kati.m.heikkonen@gmail.com", msg)