import smtplib
import datetime as dt
import random

with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r+") as file:
    content = file.read()
    content = content.replace('[NAME]', 'Krish')
    print(content)

# my_mail = "krizhnatester@gmail.com"
# password = ""
#
# now = dt.datetime.now()
# day_of_week = now.weekday()
#
# if day_of_week == 6:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_mail, password=password)
#         connection.sendmail(
#             from_addr=my_mail,
#             to_addrs="",
#             msg=f"Subject:Sunday Motivation\n\n{rand_quotes}"
#         )




