import smtplib

fromaddr = 'leonnash2008@gmail.com'
toaddr  = 'leonnash2008@hotmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'leonnash2008@gmail.com'
password = '{}'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()