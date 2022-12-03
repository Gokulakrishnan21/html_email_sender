import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Gokulakrishnan'
email['to'] = '<krishkrishnan0685@gmail.com>'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'krish'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('<gokulakrishnanofficial21@gmail.com>', '<strongpassword123@>')
        smtp.send_message(email)
        print('all good boss!')

    except:
        print("check your credentials!")
