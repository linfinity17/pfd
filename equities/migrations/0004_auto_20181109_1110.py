# Generated by Django 2.1.1 on 2018-11-09 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equities', '0003_auto_20181106_1718'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('ticker', 'tran_date')},
        ),
    ]