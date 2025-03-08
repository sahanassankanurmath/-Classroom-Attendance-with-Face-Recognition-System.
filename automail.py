import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
# path = 'Attendance'
path='Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("classtime1104@gmail.com", "nmxj ckog xfma uxlj")

# sent the mail
yag.send(
    to="classtime1104@gmail.com",
    subject=sub, # email subject
    contents="This Email From Attendacne ",  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
