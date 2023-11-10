import csv

from django.core.management.base import BaseCommand

from foodgram.settings import CSV_FILES_DIR
from recipes.models import Ingredient


class Command(BaseCommand):

    help = 'Загрузка данных об ингредиентах из CSV-файла в базу данных'

    def handle(self, *args, **options):

        with open(
            f'{CSV_FILES_DIR}/ingredients.csv', 'r', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if len(row) == 2:
                    name, measurement_unit = row
                    Ingredient.objects.create(
                        name=name,
                        measurement_unit=measurement_unit
                    )

        self.stdout.write(
            self.style.SUCCESS(
                'Успешно загружены данные об ингредиентах из CSV-файла'
            )
        )
