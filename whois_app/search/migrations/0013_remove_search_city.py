# Generated by Django 3.1.7 on 2021-02-23 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_remove_search_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='city',
        ),
    ]
