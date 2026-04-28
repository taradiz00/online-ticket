import smtplib
from email.mime.text import MIMEText
from app.core.config import settings



def get_smtp_config():
    email = settings.EMAIL_ADDRESS

    if email.endswith("@gmail.com"):
        return ("smtp.gmail.com", 465)
    
    elif email.endswith("@yahoo.com"):
        return ("smtp.mail.yahoo.com", 465)
    
    else:
        raise Exception("Unsupporter email provider")
    


def send_reset_email(to_email: str, reset_link: str):
    smtp_server, port = get_smtp_config()

    subject = "Password Reset"
    body = f"Click this link to reset your password:\n{reset_link}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_ADDRESS
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
            server.sendmail(to_email, settings.EMAIL_ADDRESS, msg.as_string())
    except Exception as e:
        print("EMAIL ERROR:", e)
print("done")