import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "mail id"
password = "password"


class Mail:
    def __init__(self):
        self.receiver_email = None
        self.name = None

    def send_mail(self):
        body = f"""\
                <html>
                  <head>
                  </head>
                  <body>
                    <h1><b>Job Spy</b></h1>
                    <p>Hi {self.name},</p>
                    <p>Attached is the job list CSV for your review. Let me know if you have any questions.</p>
                    <p>Thanks,<br><a href="LinkedIn account link">Name</a></p>
                  </body>
                </html>
                """
        subject = "Job List CSV"
        # Attach the file
        file_path = "F:/Shubham's Data/CODING/Python/web scraping/JobScraper/Jobs.csv"

        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = self.receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))

        # Attach the file
        attachment = open(file_path, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=job_list.csv")
        message.attach(part)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, self.receiver_email, message.as_string())
