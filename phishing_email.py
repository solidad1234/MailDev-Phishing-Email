import smtplib
from email.mime.text import MIMEText

# Set up the email details
sender = "admin@megacorpone.com"
recipient = "mcarlow@megacorpone.com"
subject = "Security Alert: Verify Your Account"
body = open("phishing_email.html").read()

# Create the email
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = recipient

# Send the email via MailDev
smtp = smtplib.SMTP("localhost", 1025)
smtp.sendmail(sender, recipient, msg.as_string())
smtp.quit()

print("Email sent to MailDev!")
