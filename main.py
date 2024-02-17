import pandas as pd
import datetime as dt
import credentials as cred
import random
import smtplib

birthdays = pd.read_csv('birthdays.csv')
birthdays['friend_name'] = birthdays.name # Rename column to not conflict with object.Name

now = dt.datetime.now()

for (idx, birthday) in birthdays.iterrows():
    if birthday.month == now.month and birthday.day == now.day:
        # Select letter
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as letter:
            letter_text = letter.read().replace('[NAME]', f'{birthday.friend_name}').replace('Angela', 'Will')
        
        # Send email
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls() # Makes connection secure

            connection.login(user=cred.EMAIL, password=cred.PASSWORD)
            connection.sendmail(
                from_addr=cred.EMAIL,
                to_addrs=cred.EMAIL,
                msg=f'Subject:Happy Birthday!\n\n\n{letter_text}'
            )