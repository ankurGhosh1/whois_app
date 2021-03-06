# Generated by Django 3.1.7 on 2021-02-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='creation_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='expiration_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='org',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
    ]
