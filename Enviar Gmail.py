

import smtplib
import email.message

#valid only in Gmail
def send_email():  
    body_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Subject"
    msg['From'] = 'Email From'
    msg['To'] = 'Email To'
    password = 'password created to this application in Google' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


send_email()

