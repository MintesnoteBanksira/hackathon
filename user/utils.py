from django.contrib.auth.tokens import PasswordResetTokenGenerator
import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jwt
from django.conf import settings

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) + str(user.is_active)
        )



account_activation_token = AccountActivationTokenGenerator()



def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    return token
from email.mime.text import MIMEText
from django.template.loader import render_to_string

def send_mail(mail_details):
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = os.getenv("EMAIL_HOST_USER")
        password = os.getenv("EMAIL_HOST_PASSWORD")

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = mail_details["to"]
        msg["Subject"] = mail_details["subject"]
        body = mail_details["body"]
        token = body['token']
        first_name = body['first_name']

        # decode the user from the jwt token
        decoded_token = token.decode('utf-8')

        # Default context
        context = {
            'type': 'unknown',
            'token': token,
            'first_name': first_name,
            'link': "#", 
        }

        if mail_details["subject"] == 'Activate your account':
            context['type'] = 'verification'
            context['link'] = "https://purposeify-backend-django.onrender.com/user/activate/" + decoded_token + "/"
        elif mail_details["subject"] == 'Reset Password':
            context['type'] = 'reset'
            context['link'] = "https://app.purposeify.com/reset-password/"  + decoded_token + "/"
       
        body = render_to_string('email.html', context)

        msg.attach(MIMEText(body, "html"))

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, mail_details["to"], msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Email not sent. Error: {e}")