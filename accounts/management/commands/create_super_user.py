from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    help = 'Create a superuser with an email address'

    def handle(self, *args, **options):
        username = input('Enter a username: ')
        email = input('Enter an email address: ')
        password = input('Enter a password: ')
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
