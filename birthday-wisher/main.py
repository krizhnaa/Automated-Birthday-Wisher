import smtplib
import datetime as dt
import random
import pandas as pd

now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

df = pd.read_csv("birthdays.csv")

if df[df['month'] == curr_month ]['month'].item() and df[df['day'] == curr_day ]['day'].item():
    name = df[df['month'] == curr_month ]['name'].item()


with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r+") as file:
    content = file.read()
    content = content.replace('[NAME]', f"{name}")
    print(content)

# my_mail = "krizhnatester@gmail.com"
# password = ""
#

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




