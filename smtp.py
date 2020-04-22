# Python code to illustrate Sending mail from
# your Gmail account
import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("youremail@gmail.com", "password")


message = "Message_you_need_to_send"

s.sendmail("youremail@gmail.com", "targetuseremail@gmail.com", message)

s.quit()
