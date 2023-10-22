from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings

token_generator = PasswordResetTokenGenerator()

def generate_verification_token(user):
    token = token_generator.make_token(user)
    encoded_token = urlsafe_base64_encode(force_bytes(token))
    return encoded_token

def send_verification(user):
    token = generate_verification_token(user)
    send_mail(
        subject="Email verification",
        message=f"Please click on the link to verify your email adress http://localhost:3000/verify_email/token={token}",
        from_email="noreply@lirissmile.com",
        recipient_list=["artem@weaversoft.io"],
    )