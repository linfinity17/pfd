# Generated by Django 2.1.1 on 2018-11-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equities', '0002_auto_20180926_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='alt_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='stock',
            name='sector',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
