print ("If you are seeing this, you did it wrong - correct command is nohup emailnotifier.py &")
import smtplib
from email.message import EmailMessage
#Need to add message.txt
with open (message.txt) as fp:
  msg = EmailMessage()
  msg.set_content(fp.read())
msg['Subject'] = 'You haven't practiced spelling yet today!'
msg['From'] = jgilbert4728@stu.neisd.net
msg['To'] = jgilbert4728@stu.neisd.net
