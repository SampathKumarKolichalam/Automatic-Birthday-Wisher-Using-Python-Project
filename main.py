#Importing Libraries:-
import datetime
import pandas as pd
import numpy as np
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM
import os
os.chdir(r"C:\Users\USER\Desktop\VS Code Programs\Python Programs\Birthday Wisher Project")
#os.mkdir("p")

#Getting Birthdays List:-
df=pd.read_excel("Birthdays.xlsx")
print(df)

#Send_Mail function with all sender and reciver info:-
def email_func(subject,reciever_mail,name):
  receiver=reciever_mail
  sender_mail_id="kolichalamsampathkumar@gmail.com"
  sender_mail_password=""
     
  #MIMEMultipart Object:-
  msg=MM()
  msg["Subject"]=subject+" "+str(name)+"!"
    
  #HTML For Message:-
  HTML="""
    <html>
       <body>
           <h1>Happy Birthday!</h1>.
           <img src="https://cdn.pixabay.com/photo/2018/02/12/16/40/birthday-3148707__340.png" alt="Image" width="640" height="360"></img>
           <h2>
               <p>Hello<br>
                I Hope you have a Wonderful day ! <br><br>
                From;<br>
                Your Friend
                </p>
           </h2>
        </body>
    </html>
"""

  #HTML MIMETEXT Object:-
  MTObj=MT(HTML,"html")

#Attach the MIMETEXT Object into message:-
  msg.attach(MTObj)

#SSL Creation:-
  SSL_context=ssl.create_default_context()

#SMTP Creation:-
  server=smtplib.SMTP_SSL(host="smtp.gmail.com",port=465,context=SSL_context)
  server.login(sender_mail_id,sender_mail_password)
  server.sendmail(sender_mail_id,reciever_mail,msg.as_string())

#Today date:-
today=datetime.date.today()
year=today.year

#Looping through Birthdays:-
for i in range(0,len(df)):
  month=df["Birth_month"][i]
  day=df["Birth_day"][i]
  name=df["Name"][i]
  email=df["Email"][i]
  birthdate=datetime.date(year,month,day)

#Checking today is birthday or not:-
  if birthdate==today:
    email_func("Happy Birthday",email,name)
    print("Wishes sent")
  else:
    print("Wishes not sent")
