# Generated by Django 4.0.4 on 2022-05-18 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='cheque_micr',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='draft_micr',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
