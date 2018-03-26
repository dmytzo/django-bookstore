from django.core.management.base import BaseCommand, CommandError
from bookstore_management.models import Book


class Command(BaseCommand):
    help = "Ordered book list"

    def add_arguments(self, parser):
        parser.add_argument(
            '--desc',
            default=False,
        )
        parser.add_argument(
            '--asc',
            default=False,
        )

    def handle(self, *args, **options):
        if options['desc']:
            books = Book.objects.all().order_by('-publish_date')
        else:
            books = Book.objects.all().order_by('publish_date')
        for book in books:
            book_command = {
                            'title': book.book_title,
                            'ISBN': book.ISBN,
                            'price': book.price,
                            'publish_date': book.publish_date.strftime('%m/%d/%Y')
                            }
            self.stdout.write(str(book_command))
