import logging

import azure.functions as func
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = Mail(
    from_email='khoalnn@icloud.com',
    to_emails='lekhoa248@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return func.HttpResponse(
         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
         status_code=200)
    except Exception as e:
        print(e.message)
        return func.HttpResponse(
         e.message,
         status_code=500)