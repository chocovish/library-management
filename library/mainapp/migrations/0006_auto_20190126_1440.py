# Generated by Django 2.1.5 on 2019-01-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_user_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrow_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
