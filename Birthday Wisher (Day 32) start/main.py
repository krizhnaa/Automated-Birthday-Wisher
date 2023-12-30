import smtplib

my_mail = "krizhnatester@gmail.com"
password = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=password)
connection.sendmail(from_addr=my_mail, to_addrs="", msg="Heyy")
connection.close()

