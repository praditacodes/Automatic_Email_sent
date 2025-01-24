

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication


#email credentials

sender_email= "exaple@gmail.com"
receiver_email = "example@gmail.com"
password=" wwww eeee tttt tttt"#your app password  exaple 
file_to_send=("Email.csv")

message= MIMEMultipart()
message["FROM"] = sender_email
message["To"] = receiver_email
message["SUBJECT"]= "Test Email"


#email body
body= "Hello , This is ta test email send from python  using automation"
message.attach(MIMEText(body, "plain"))


fp = open(file_to_send)
    
attachment = MIMEText(fp.read())
fp.close()
attachment.add_header("Content-Disposition", "attachment", filename=file_to_send)
message.attach(attachment)

     
#send the email
try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message.as_string())
    print("Email sent succesfully")
except Exception as  e:
    print(f"Error:{e}")
