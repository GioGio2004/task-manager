
import smtplib


password = ""


email = ""
reciever_email = ""
subject = ""
message = ""

text = f"{subject} \n {message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

def send_email(text):
    server.login(email, password)
    server.sendmail(email, reciever_email, text)

print(f"mail has been sent to {reciever_email}")
