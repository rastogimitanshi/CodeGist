import csv
import smtplib
from setting import SENDER_EMAIL, SENDER_PASSWORD

ACCEPTED_MSG="""
Hi {},

This is a test email to tell you that your application has beem accepted to join
the "Cats Group of University".
We hope you have a great time here!
Best Of Luck!

Email : {}
ACCEPTANCE - {}

Regards,
Mitanshi
"""
REJECTED_MSG ="""
Hi {}

This is a test email to tell that your application to join "Cats Group
of University" has been rejected. Don't lose hope and apply next year. Good luck for your future.


Email : {}
ACCEPTANCE - {}

Regards,
Mitanshi
"""
csv_file = open('application.csv')
csv_reader =csv.reader(csv_file,delimiter=',')
next(csv_reader)
smtp = smtplib.SMTP('smtp.gmail.com',587)
smtp.starttls()
smtp.login(SENDER_EMAIL,SENDER_PASSWORD)
for row in csv_reader:
    name,email,friend = row
    print(name,email,friend)
    if(friend=="yes"):
        msg = FRIEND_MSG.format(name,email,friend)
        subject ="FRIEND"
    else:
        msg = NOTFRIEND_MSG.format(name,email,name,friend)
        subject = "NOT FRIEND"
    #email_msg ="Subject: {} \n\n {}",format(subject,msg) 
    smtp.sendmail(SENDER_EMAIL,'mitanshi1995.mr@gmail.com',msg)
    print("Send email to: {}",format(email))
    print("Email Content:\n")
    print(msg)
csv_file.close()
smtp.quit()
