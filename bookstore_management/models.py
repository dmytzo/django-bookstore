import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete


class Book(models.Model):
    book_title = models.CharField(max_length=40)
    authors_info = models.CharField(max_length=120, blank=True)
    ISBN = models.PositiveIntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='book-images/', blank=True)
    publish_date = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return self.book_title

    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)
        super(Book, self).delete(*args, **kwargs)


class RequestLog(models.Model):
    url = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url


def book_saved_and_edited_receiver(sender, instance, created, **kwargs):
    logger = logging.getLogger('bookstore_management.views')
    if created:
        logger.info('created')
    else:
        logger.info('updated')


def book_deleted_receiver(sender, instance, using, **kwargs):
    logger = logging.getLogger('bookstore_management.views')
    logger.info('deleted')


post_save.connect(book_saved_and_edited_receiver, sender=Book)
post_delete.connect(book_deleted_receiver, sender=Book)
