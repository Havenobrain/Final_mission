from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def disable_signup(sender, **kwargs):
    raise Exception("Registration is disabled.")
