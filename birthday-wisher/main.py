import smtplib
import datetime as dt
import random
import pandas as pd

my_mail = "krizhnatester@gmail.com"
password = ""

now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

df = pd.read_csv("birthdays.csv")

try:
    if df[df['month'] == curr_month ]['month'].item() and df[df['day'] == curr_day ]['day'].item():
        name = df[df['month'] == curr_month ]['name'].item()

        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r+") as file:
            content = file.read()
            content = content.replace('[NAME]', f"{name}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs="",
                msg=f"Subject:Happy Birthday {name}\n\n{content}"
            )
except ValueError:
    print("Not anyone's Birthday Today")








