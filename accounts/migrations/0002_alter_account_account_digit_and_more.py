# Generated by Django 4.0.6 on 2022-07-17 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_digit',
            field=models.CharField(editable=False, max_length=1, verbose_name='Digit'),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(editable=False, max_length=5, verbose_name='Account'),
        ),
    ]