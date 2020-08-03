from datetime import datetime

from django.core.management import BaseCommand

from order.models import Order, User


class Command(BaseCommand):
    help = 'Load test data from csv file'

    def handle(self, *args, **options):
        with open("test_data/TestData.csv") as csv_file:
            csv_lines = csv_file.read().splitlines()
            for line in csv_lines[1:]:
                user_data = line.split(',')
                first_name = user_data[0]
                last_name = user_data[1]
                User.objects.update_or_create(
                    username=f'{first_name}_{last_name}',
                    defaults={
                        'first_name': first_name,
                        'last_name': last_name,
                        'birth_date': datetime.strptime(user_data[2], '%Y/%m/%d'),
                        'registration_date': datetime.strptime(user_data[3], '%Y/%m/%d'),
                    }
                )
