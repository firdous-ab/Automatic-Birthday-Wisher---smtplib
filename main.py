from datetime import datetime
import pandas
import random
import smtplib


MY_EMAIL = "damilolabakare222@gmail.com"
MY_PASSWORD = "arvmutrfpxdomrhh"

month = datetime.now().month
day = datetime.now().day
today_tuple = (month, day)
# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# Use dictionary comprehension to create a dictionary from birthday.csv
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
# Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and
    # replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=60) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Ajokebakaredam2004@outlook.com",
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
