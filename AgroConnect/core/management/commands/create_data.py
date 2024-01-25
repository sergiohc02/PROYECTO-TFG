from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Este comando sirve para crear toda la información falsa de la base de datos"

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        raise NotImplementedError()
