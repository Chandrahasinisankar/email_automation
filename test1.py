from email.mime.application import MIMEApplication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, app_password, attachment_path):
    email = 'sankarchandrahasini@gmail.com'
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name='attached_file')
            part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
            message.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()

        try:
            server.ehlo()
            server.login(email, app_password)
            server.sendmail(email, to_email, message.as_string())
            print(f"Email sent to {to_email} successfully.")
        
        except smtplib.SMTPException as e:
            print(f"SMTP Exception: {e}")

app_password = "iyyz zjym xvib cygy" 
subject = input("enter subject : ")
body = input("enter body : ")
recipient_email = input("enter a valid mail id : ")  
attachment_path = input(r"Enter the path to the attachment (optional, press Enter to skip) : ")
send_email(subject, body, recipient_email, app_password, attachment_path)