#import RPi.GPIO as GPIO
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
gmail_user = "shrutipasumarti@gmail.com"
gmail_pwd = input('enter the password :')
if (gmail_pwd == "Shruti123*") :
    FROM = 'shrutipasumarti@gmail.com'
    TO = ['pshruts2000@gmail.com'] #must be a list




else :

     FROM = 'shrutipasumarti@gmail.com'
     TO = ['pshruts2000@gmail.com'] #must be a list
     msg = MIMEMultipart()
     time.sleep(1)
     msg['Subject'] ="Alert"
     body="SECURITY BREACH ALERT"
     msg.attach(MIMEText(body,'plain'))
     time.sleep(1)



#BODY with 2 argument

#body=sys.argv[1]+sys.argv[2]


try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        print ("smtp.gmail")
        server.ehlo()
        print ("ehlo")
        server.starttls()
        print ("starttls")
        server.login(gmail_user, gmail_pwd)
        print ("reading mail & password")
        server.sendmail(FROM, TO, msg.as_string())
        print ("from")
        server.close()
        print ('successfully sent the mail')
except:
        print ("failed to send mail")
