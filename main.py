# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime
import pandas as pd
import random
import smtplib
import os

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

birthdays = pd.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    name = row["name"]
    birthday = (row.month, row.day)
    if birthday == today:
        letter_template = random.choice(letter_templates)
        with open(f"letter_templates/{letter_template}") as template:
            content = template.read()
            content = content.replace("[NAME]", name)
        # print(content)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=f"Subject:Happy Birthday!\n\n{content}")
