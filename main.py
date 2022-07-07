
from datetime import datetime
import random
import smtplib
import pandas

My_email = 0
Password = 0

today = (datetime.now().month, datetime.now().date)
data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(13)}.txt'
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(My_email, Password)
        connection.sendmail(from_addr=My_email, to_addrs=birthday_person['email'], msg=f'Subject: Happy Birthday!\n\n{content}')