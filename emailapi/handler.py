import json
import smtplib
from email.mime.text import MIMEText


# Function to send email
def send_email(event, context):

    try:
        data = json.loads(event['body'])
        receiver = data['receiver_email']
        subject = data['subject']
        body = data['body_text']

        sender_email = 'mirzamerajbaig1992@gmail.com'
        sender_password = 'denc fwqq ktqm keju'

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver

        # Send email using Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())

            
        return {

            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully!'})
        }
    
    except KeyError as e:
        return {

            'statusCode': 400,
            'body': json.dumps({'error': f'Missing field: {str(e)}'})
        }

    except Exception as e:
        return {

            'statusCode': 500,
            'body': json.dumps({'error': f'Internal Server Error: {str(e)}'})
        }