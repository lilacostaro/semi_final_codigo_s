# Generated by Django 4.0.6 on 2022-07-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_rename_account_id_transactions_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='account_number',
            field=models.CharField(max_length=5),
        ),
    ]
