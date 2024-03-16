from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL="onal052001@gmail.com"
MY_PASSWORD="lxaxkgpxdimpqgpt"

today=datetime.now()
today_tuple = (today.month, today.day)

data=pandas.read_csv("birthdays.csv")           #Use pandas to read the birthdays.csv

#Use dictionary comprehension to create a dict from birthday.csv that is formated like this
#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
#Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path)as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])  #If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
        #Use the replace() method to replace[NAME] the actual name.

    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


