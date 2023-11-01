from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random
import string

User = get_user_model()

class RegistrationService:
    def register_user(self, email, password):
        user = User.objects.create_user(email=email, password=password)
        confirmation_code = self.generate_confirmation_code()
        user.confirmation_code = confirmation_code
        user.save()
        self.send_confirmation_email(user, confirmation_code)

    def generate_confirmation_code(self, length=6):
        return ''.join(random.choices(string.digits, k=length))

    def send_confirmation_email(self, user, code):
        subject = 'Подтверждение регистрации'
        message = f'Код подтверждения: {code}'
        from_email = 'noreply@example.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

class ConfirmationService:
    def confirm_registration(self, user, code):
        if code == user.confirmation_code:
            user.is_active = True
            user.save()