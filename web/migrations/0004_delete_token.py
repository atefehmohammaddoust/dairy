# Generated by Django 3.0.3 on 2020-03-10 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200309_1608'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Token',
        ),
    ]