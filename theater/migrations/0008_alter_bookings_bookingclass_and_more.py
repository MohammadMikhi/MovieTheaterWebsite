# Generated by Django 4.0.6 on 2022-08-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0007_alter_bookings_bookingclass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='bookingClass',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='paymentMethod',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='showingTime',
            field=models.CharField(max_length=50),
        ),
    ]
