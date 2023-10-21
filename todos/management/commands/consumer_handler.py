from django.core.management.base import BaseCommand
from todos.consumer import NotificationConsumer


class Command(BaseCommand):
    help = 'Launches Listener for user_created message : Kafka'

    def handle(self, *args, **options):
        td = NotificationConsumer()
        td.start()
        self.stdout.write("Started Consumer Thread")
