#Simple Mail transfer protocol

# import smtplib

my_email = "sabiha@gmail.com"
password = "12341234*"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sultana@gmail.com", msg="Hello\n\nHave a good day")


# Datetime library python

import datetime as dt

now = dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.weekday())
print(type(now.hour))

#creating  a date time
D_O_B = dt.datetime(year=1990, month=3, day=4, hour=8 )
print(D_O_B)

