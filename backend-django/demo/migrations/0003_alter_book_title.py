# Generated by Django 3.2 on 2021-04-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
