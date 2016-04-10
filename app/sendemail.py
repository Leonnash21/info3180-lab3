import smtplib

def send_email(name, email, subject, new_message):
    fromaddr = 'leonnash2008@gmail.com'
    toaddr = 'leonnash2008@hotmail.com'
    fromname = 'Leon'
    toname = 'Leon nash'
    
    message = """
        From: {} <{}>
        To: {} <{}>
        Subject: {}
        {}
        """

    messagetosend = message.format(
        name,
        email,
        toname,
        toaddr,
        subject,
        new_message)

    username = "leonnash2008@gmail"
    password = ""

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, messagetosend)
    server.quit()
