from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a default user if not exists'

    def handle(self, *args, **kwargs):
        username = 'default_user'
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password='default_password')
            print(f"User '{username}' created.")
        else:
            print(f"User '{username}' already exists.")
