#imports
import smtplib
import random 
import pandas
from datetime import datetime


#  Checking if today matches a birthday in the CSV File

today=datetime.now()
today_date=(today.month,today.day)


birthdays_data=pandas.read_csv("birthdays.csv")


#creating a dictionary that have months and days extracted from each row in the data base !
birthdays_dict={(data["month"],data["day"]):data for(index,data) in birthdays_data.iterrows()} 

#checking if today has anyone birthday
if (today_date) in birthdays_dict:
  birthday_person=birthdays_dict[today_date] #checking the person behind this date 
  
  PLACEHOLDER='[NAME]' #the blank mwe want to replace 
  letter=f"letter_{random.randint(1,3)}.txt" #choosing a random quote to be sended
  
  with  open(letter) as letter_file:
    letter_quote=letter_file.read() #reading the file to modify it
    new_letter=letter_quote.replace(PLACEHOLDER,birthday_person["name"]) #replacing the Name blank by the actuall name who have BD .

# Sending  the letter generated above :
  
  with smtplib.SMTP("smtp.gmail.com") as connection :

    connection.starttls()
    connection.login(user='Your Email',password='Your Password')
    connection.sendmail(from_addr="Your Email",to_addrs=birthday_person[" Recipient Email"],msg= f"subject:Happy birthday \n\n {new_letter}")
    connection.close()