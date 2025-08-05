import smtplib
from email.message import EmailMessage

# ——— USER CONFIG ———
my_email = "your email"
app_password = "your app password"   # your 16-char Gmail App Password, no spaces
recipient = "recipient email"
# ——————————————

# 1) Build the message
msg = EmailMessage()
msg["Subject"] = "hello bro long time no see"
msg["From"] = my_email
msg["To"] = recipient
msg.set_content("This is me bro—hello world")

# 2) Send via SMTP over SSL
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(my_email, app_password)
    smtp.send_message(msg)

print("Email sent successfully!")
