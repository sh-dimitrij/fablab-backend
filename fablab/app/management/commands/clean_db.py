from django.core.management.base import BaseCommand
from ...models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        Work.objects.all().delete()
        CustomUser.objects.all().delete()