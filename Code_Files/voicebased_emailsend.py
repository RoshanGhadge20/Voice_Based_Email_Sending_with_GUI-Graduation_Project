'''This file is having voice based email sending using Smtplib'''

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage




def sendmail():
    listener = sr.Recognizer()
    engine = pyttsx3.init()

    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def get_info():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                info = listener.recognize_google(voice)
                print(info)
                return info.lower()
        except:
            pass


    def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Make sure to give app access in your Google account
        server.login('shubhamghadge195353', '$HUBH@M928')
        email = EmailMessage()
        email['From'] = 'shubhamghadge195353@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)


    email_list = {
        'roshan': 'roshanghadge20@gmail.com',
        'shubham': 'shubhamghadge559@gmail.com',
        'ghadge': 'ghadgeshubham559@gmail.com',
        'shubham1': 'shubhamghadge195353@gmail.com'
    }



    def get_email_info():
        talk('To Whom you want to send email')
        name = get_info()
        receiver =email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = get_info()
        talk('what is the text in your email')
        message = get_info()
        send_email(receiver, subject, message)
        talk('Your email is sent')
        print('Your email is sent')


    get_email_info()
#sendmail()

