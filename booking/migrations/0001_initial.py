# Generated by Django 5.0.7 on 2024-07-27 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_name', models.CharField(max_length=40)),
                ('telephone_number', models.IntegerField(default='')),
                ('number_of_people', models.PositiveIntegerField(help_text='For bookings greater than 8 people, please call us at 01 2340000.')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00')], max_length=5)),
                ('comments', models.CharField(max_length=200, null=True)),
                ('reservation_date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-reservation_date'],
            },
        ),
    ]
