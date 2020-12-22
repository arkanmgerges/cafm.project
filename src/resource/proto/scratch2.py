import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='bounces+19695021@em5198.supercafm.com',
    to_emails='arkan.m.gerges@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>hello world</strong>')

try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
    print(e.body)