# Generated by Django 2.0.3 on 2018-03-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
