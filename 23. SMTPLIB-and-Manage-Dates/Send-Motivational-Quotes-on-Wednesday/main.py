# sends email every wednesday with a motivationl quote
import random
import datetime as dt
import smtplib



with open("quotes.txt") as file:
    data = file.readlines()
    # print(data)

def send_email():


    my_email = "SENDER.EMAIL@gmail.com"
    password = "12341234*"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="RECIEVER.EMAIL@gmail.com", msg=f"Subject:Quote of the week\n\n {quote}")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    quote = random.choice(data)
    send_email()

