# Generated by Django 4.0.4 on 2022-05-18 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10)),
                ('date_donation', models.DateTimeField(auto_now_add=True)),
                ('mode_donation', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Draft', 'Draft')], default='Cash', max_length=10)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('cheque_no', models.CharField(blank=True, max_length=6, null=True)),
                ('cheque_micr', models.CharField(blank=True, max_length=6, null=True)),
                ('cheque_date', models.DateField(blank=True, null=True)),
                ('cheque_amount', models.IntegerField(blank=True, null=True)),
                ('draft_no', models.CharField(blank=True, max_length=6, null=True)),
                ('draft_micr', models.CharField(blank=True, max_length=6, null=True)),
                ('draft_date', models.DateField(blank=True, null=True)),
                ('draft_amount', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
