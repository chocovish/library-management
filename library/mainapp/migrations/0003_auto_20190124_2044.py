# Generated by Django 2.1.5 on 2019-01-24 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
