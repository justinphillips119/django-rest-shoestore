from django.core.management.base import BaseCommand, CommandError

from api_app.models import Manufacturer, ShoeType, ShoeColor, Shoe



class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        shoe_type = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        for shoe in shoe_type:
            ShoeType.objects.create(style=shoe)
        shoe_color = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black']
        for shoe in shoe_color:
            ShoeColor.objects.create(color_name=shoe)